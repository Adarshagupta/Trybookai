import os
from dotenv import load_dotenv
import time
import traceback
from flask import Flask, render_template, request, jsonify, send_file, Response
import openai
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import io
import asyncio
import aiohttp
from queue import Queue

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

progress_queue = Queue()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

async def generate_chunk(model, topic, current_word_count, language, is_new_chapter=False):
    if is_new_chapter:
        prompt = f"Write the beginning of a new chapter for a book about {topic} in {language}. This is around word {current_word_count} of the book. Start with a chapter title."
    else:
        prompt = f"Continue writing a book about {topic} in {language}. This is around word {current_word_count} of the book. Make sure the narrative flows smoothly from the previous section."
    
    try:
        async with aiohttp.ClientSession() as session:
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
        return await generate_chunk(model, topic, current_word_count, language, is_new_chapter)

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

    story = []

    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 24))

    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith("Chapter"):
            story.append(Spacer(1, 24))
            story.append(Paragraph(line.strip(), styles['Chapter']))
        else:
            story.append(Paragraph(line, styles['Content']))

    doc.build(story)
    buffer.seek(0)
    return buffer

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/playground')
def playground():
    return render_template('index.html')
@app.route('/generate', methods=['POST'])
async def generate_book():
    model = request.form['model']
    topic = request.form['topic']
    language = request.form['language']
    target_word_count = int(request.form['word_count'])
    current_word_count = 0
    book_content = []
    chapter_count = 0

    tasks = []
    while current_word_count < target_word_count:
        is_new_chapter = (chapter_count == 0) or (current_word_count > 0 and current_word_count % 3000 < 500)
        
        if is_new_chapter:
            chapter_count += 1
            task = asyncio.create_task(generate_chunk(model, topic, current_word_count, language, is_new_chapter=True))
        else:
            task = asyncio.create_task(generate_chunk(model, topic, current_word_count, language))
        
        tasks.append(task)
        current_word_count += 500  # Approximate word count per chunk
        
        if len(tasks) >= 5 or current_word_count >= target_word_count:
            chunks = await asyncio.gather(*tasks)
            for chunk in chunks:
                book_content.append(chunk)
                actual_word_count = len(" ".join(book_content).split())
                progress_queue.put(actual_word_count)
            tasks = []
            await asyncio.sleep(1)  # Small delay to avoid rate limits

    formatted_book = "\n\n".join(book_content)
    actual_word_count = len(formatted_book.split())

    return jsonify({
        'content': formatted_book,
        'word_count': actual_word_count
    })


@app.route('/progress')
def progress():
    def generate(): 
        while True:
            if not progress_queue.empty():
                yield f"data: {progress_queue.get()}\n\n"
            else:
                yield "data: keep-alive\n\n"
            time.sleep(1)
    
    return Response(generate(), mimetype='text/event-stream')

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    try:
        content = request.json['content']
        title = request.json['title']
        language = request.json['language']
        pdf_buffer = create_pdf(content, title, language)
        
        return send_file(pdf_buffer, download_name=f"{title}.pdf", as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        app.logger.error(f"PDF download error: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5151)