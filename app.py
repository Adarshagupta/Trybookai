import os
from dotenv import load_dotenv
import time
import traceback
from flask import Flask, render_template, request, jsonify, send_file, Response, stream_with_context
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import io
from cachetools import TTLCache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()

app = Flask(__name__)

# Initialize rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Initialize cache
cache = TTLCache(maxsize=100, ttl=300)  # Cache size of 100, TTL of 5 minutes

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Database connection
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

# Initialize PostgreSQL database
def init_db():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS pdfs
                         (id SERIAL PRIMARY KEY,
                          ip TEXT,
                          title TEXT,
                          filepath TEXT,
                          timestamp TIMESTAMP)''')
        conn.commit()

init_db()

async def generate_chunk(session, model, topic, current_word_count, language, is_new_chapter=False):
    prompt = f"{'Write the beginning of a new chapter' if is_new_chapter else 'Continue writing'} for a book about {topic} in {language}. This is around word {current_word_count} of the book. {'Start with a chapter title.' if is_new_chapter else 'Make sure the narrative flows smoothly from the previous section.'}"
    
    try:
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": f"You are an author writing a book in {language}. Format your response as a part of a book chapter."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 3000
            }
        ) as response:
            result = await response.json()
            if 'choices' not in result or len(result['choices']) == 0:
                raise ValueError(f"Unexpected API response: {result}")
            return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        await asyncio.sleep(60)
        return await generate_chunk(session, model, topic, current_word_count, language, is_new_chapter)

def create_pdf(content, title, language):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    styles = getSampleStyleSheet()
    
    font = 'Helvetica'
    
    styles.add(ParagraphStyle(name='Chapter',
                              fontName=font,
                              fontSize=18,
                              spaceAfter=12,
                              alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Content',
                              fontName=font,
                              fontSize=12,
                              spaceAfter=12,
                              alignment=TA_JUSTIFY))

    story = [
        Paragraph(title, styles['Title']),
        Spacer(1, 24)
    ]

    for line in content.split('\n'):
        if line.strip().startswith("Chapter"):
            story.extend([Spacer(1, 24), Paragraph(line.strip(), styles['Chapter'])])
        else:
            story.append(Paragraph(line, styles['Content']))

    doc.build(story)
    buffer.seek(0)
    return buffer

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/playground')
def playground():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
@limiter.limit("5 per minute")
def generate_book():
    model = request.form['model']
    topic = request.form['topic']
    language = request.form['language']
    target_word_count = int(request.form['word_count'])

    async def generate():
        current_word_count = 0
        book_content = []
        chapter_count = 0

        async with aiohttp.ClientSession() as session:
            while current_word_count < target_word_count:
                is_new_chapter = (chapter_count == 0) or (current_word_count > 0 and current_word_count % 3000 < 500)
                
                if is_new_chapter:
                    chapter_count += 1

                chunk = await generate_chunk(session, model, topic, current_word_count, language, is_new_chapter)
                book_content.append(chunk)
                current_word_count = len(" ".join(book_content).split())
                
                yield f"data: {current_word_count}\n\n"
                
                await asyncio.sleep(1)  # Small delay to avoid rate limits

        formatted_book = "\n\n".join(book_content)
        yield f"data: {formatted_book}\n\n"

    def generate_wrapper():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        gen = generate()
        try:
            while True:
                try:
                    item = loop.run_until_complete(gen.__anext__())
                    yield item
                except StopAsyncIteration:
                    break
        finally:
            loop.run_until_complete(gen.aclose())
            loop.close()

    return Response(stream_with_context(generate_wrapper()), mimetype='text/event-stream')

@app.route('/download-pdf', methods=['POST'])
@limiter.limit("10 per minute")
def download_pdf():
    try:
        content = request.json['content']
        title = request.json['title']
        language = request.json['language']
        pdf_buffer = create_pdf(content, title, language)
        
        ip = request.remote_addr
        timestamp = datetime.now()
        filename = f"{ip}_{timestamp.strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join('saved_pdfs', filename)
        os.makedirs('saved_pdfs', exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(pdf_buffer.getvalue())
        
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO pdfs (ip, title, filepath, timestamp) VALUES (%s, %s, %s, %s)",
                            (ip, title, filepath, timestamp))
            conn.commit()
        
        return send_file(io.BytesIO(pdf_buffer.getvalue()), download_name=f"{title}.pdf", as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        app.logger.error(f"PDF download error: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/save-pdf', methods=['POST'])
@limiter.limit("10 per minute")
def save_pdf():
    try:
        content = request.json['content']
        title = request.json['title']
        language = request.json['language']
        ip = request.remote_addr
        timestamp = datetime.now()
        
        pdf_buffer = create_pdf(content, title, language)
        
        filename = f"{ip}_{timestamp.strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join('saved_pdfs', filename)
        os.makedirs('saved_pdfs', exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(pdf_buffer.getvalue())
        
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO pdfs (ip, title, filepath, timestamp) VALUES (%s, %s, %s, %s)",
                            (ip, title, filepath, timestamp))
            conn.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        app.logger.error(f"PDF save error: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/get-saved-pdfs', methods=['GET'])
@limiter.limit("30 per minute")
def get_saved_pdfs():
    try:
        ip = request.remote_addr
        cache_key = f'saved_pdfs_{ip}'
        cached_result = cache.get(cache_key)
        if cached_result:
            return jsonify({'pdfs': cached_result})

        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, title, timestamp FROM pdfs WHERE ip = %s ORDER BY timestamp DESC", (ip,))
                pdfs = cur.fetchall()
        
        cache[cache_key] = pdfs
        return jsonify({'pdfs': pdfs})
    except Exception as e:
        app.logger.error(f"Get saved PDFs error: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/download-saved-pdf/<int:pdf_id>', methods=['GET'])
@limiter.limit("10 per minute")
def download_saved_pdf(pdf_id):
    try:
        ip = request.remote_addr
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT filepath, title FROM pdfs WHERE id = %s AND ip = %s", (pdf_id, ip))
                result = cur.fetchone()
        
        if result is None:
            return jsonify({'error': 'PDF not found or unauthorized'}), 404
        
        filepath, title = result['filepath'], result['title']
        return send_file(filepath, download_name=f"{title}.pdf", as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        app.logger.error(f"Download saved PDF error: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5151)
