import time
import traceback
from flask import Flask, render_template, request, jsonify, send_file
import openai
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import io
import asyncio
import aiohttp

app = Flask(__name__)

async def generate_chunk(api_key, model, topic, current_word_count, is_new_chapter=False):
    openai.api_key = api_key
    if is_new_chapter:
        prompt = f"Write the beginning of a new chapter for a book about {topic}. This is around word {current_word_count} of the book. Start with a chapter title."
    else:
        prompt = f"Continue writing a book about {topic}. This is around word {current_word_count} of the book. Make sure the narrative flows smoothly from the previous section."
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are an author writing a book. Format your response as a part of a book chapter."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": 500
                }
            ) as response:
                result = await response.json()
                return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        await asyncio.sleep(60)
        return await generate_chunk(api_key, model, topic, current_word_count, is_new_chapter)

def create_pdf(content, title):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Chapter',
                              fontSize=18,
                              spaceAfter=12,
                              alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Content',
                              fontSize=12,
                              spaceAfter=12,
                              alignment=TA_JUSTIFY))

    story = []

    # Add title
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 24))

    # Add content
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
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
async def generate_book():
    api_key = request.form['api_key']
    model = request.form['model']
    topic = request.form['topic']
    target_word_count = int(request.form['word_count'])
    current_word_count = 0
    book_content = []
    chapter_count = 0

    tasks = []
    while current_word_count < target_word_count:
        is_new_chapter = (chapter_count == 0) or (current_word_count > 0 and current_word_count % 3000 < 500)
        
        if is_new_chapter:
            chapter_count += 1
            task = asyncio.create_task(generate_chunk(api_key, model, topic, current_word_count, is_new_chapter=True))
        else:
            task = asyncio.create_task(generate_chunk(api_key, model, topic, current_word_count))
        
        tasks.append(task)
        current_word_count += 500  # Approximate word count per chunk
        
        if len(tasks) >= 5 or current_word_count >= target_word_count:
            chunks = await asyncio.gather(*tasks)
            for i, chunk in enumerate(chunks):
                if i == 0 and is_new_chapter:
                    chunk = f"\n\nChapter {chapter_count}\n\n" + chunk
                book_content.append(chunk)
            tasks = []
            await asyncio.sleep(1)  # Small delay to avoid rate limits

    formatted_book = "\n\n".join(book_content)
    actual_word_count = len(formatted_book.split())

    return jsonify({
        'content': formatted_book,
        'word_count': actual_word_count
    })

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    try:
        content = request.json['content']
        title = request.json['title']
        pdf_buffer = create_pdf(content, title)
        
        return send_file(pdf_buffer, download_name=f"{title}.pdf", as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        app.logger.error(f"PDF download error: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)