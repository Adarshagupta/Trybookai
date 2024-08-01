import openai
import time
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="Open_ai_api")  # Replace with your actual API key

def generate_chunk(topic, current_word_count):
    prompt = f"Continue writing a book about {topic}. This is around word {current_word_count} of the book. Make sure the narrative flows smoothly from the previous section."
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an author writing a book."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except openai.RateLimitError:
        print("Rate limit exceeded. Waiting for 60 seconds before retrying...")
        time.sleep(60)
        return generate_chunk(topic, current_word_count)

def main():
    topic = input("Enter the topic for your book: ")
    output_file = "generated_book.txt"
    target_word_count = 100000
    current_word_count = 0
    
    with open(output_file, "w", encoding="utf-8") as file:
        while current_word_count < target_word_count:
            chunk = generate_chunk(topic, current_word_count)
            words = chunk.split()
            chunk_word_count = len(words)
            
            if current_word_count + chunk_word_count > target_word_count:
                words = words[:target_word_count - current_word_count]
                chunk = " ".join(words)
            
            file.write(chunk + "\n\n")
            current_word_count += len(words)
            print(f"Generated {current_word_count} words...")
            
            # Add a small delay to avoid hitting rate limits
            time.sleep(1)
    
    print(f"Book generation complete. {current_word_count} words have been generated and saved to {output_file}")

if __name__ == "__main__":
    main()