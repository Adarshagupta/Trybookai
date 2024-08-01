import time
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

def generate_chunk(api_key, topic, current_word_count, is_new_chapter=False):
    client = OpenAI(api_key=api_key)
    if is_new_chapter:
        prompt = f"Write the beginning of a new chapter for a book about {topic}. This is around word {current_word_count} of the book. Start with a chapter title."
    else:
        prompt = f"Continue writing a book about {topic}. This is around word {current_word_count} of the book. Make sure the narrative flows smoothly from the previous section."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an author writing a book. Format your response as a part of a book chapter."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)
        return generate_chunk(api_key, topic, current_word_count, is_new_chapter)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_book():
    api_key = request.form['api_key']
    topic = request.form['topic']
    target_word_count = int(request.form['word_count'])
    current_word_count = 0
    book_content = []
    chapter_count = 0

    while current_word_count < target_word_count:
        is_new_chapter = (chapter_count == 0) or (current_word_count > 0 and current_word_count % 3000 < 500)
        
        if is_new_chapter:
            chapter_count += 1
            chunk = f"\n\nChapter {chapter_count}\n\n" + generate_chunk(api_key, topic, current_word_count, is_new_chapter=True)
        else:
            chunk = generate_chunk(api_key, topic, current_word_count)
        
        words = chunk.split()
        chunk_word_count = len(words)
        
        if current_word_count + chunk_word_count > target_word_count:
            words = words[:target_word_count - current_word_count]
            chunk = " ".join(words)
        
        book_content.append(chunk)
        current_word_count += len(words)
        
        # Add a small delay to avoid hitting rate limits
        time.sleep(1)

    formatted_book = "\n\n".join(book_content)

    return jsonify({
        'content': formatted_book,
        'word_count': current_word_count
    })

if __name__ == "__main__":
    app.run(debug=True)