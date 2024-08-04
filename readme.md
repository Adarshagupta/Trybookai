# BookAI


BookAI is an advanced Flask-based web application that leverages OpenAI's state-of-the-art language models to generate full-length books on any topic. This powerful tool allows users to customize various parameters to create unique, coherent, and engaging books, complete with chapter structures and formatted content.


## Table of Contents


1. [Features](#features)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
   - [Basic Usage](#basic-usage)
   - [Advanced Usage](#advanced-usage)
7. [API Reference](#api-reference)
8. [Docker Deployment](#docker-deployment)
9. [Development](#development)
   - [Project Structure](#project-structure)
   - [Adding New Features](#adding-new-features)
   - [Testing](#testing)
10. [Performance Optimization](#performance-optimization)
11. [Troubleshooting](#troubleshooting)
12. [Contributing](#contributing)
13. [License](#license)
14. [Disclaimer](#disclaimer)


## Features


- Generate complete books on any topic using OpenAI's GPT models
- Support for multiple languages with coherent narrative flow
- Dynamic chapter generation and structure
- Real-time progress tracking with server-sent events
- Asynchronous content generation for improved performance
- PDF generation with customizable formatting
- Configurable API usage to manage token consumption
- Error handling and automatic retries for API failures


## Architecture


BookAI follows a client-server architecture:


- **Frontend**: HTML/CSS/JavaScript for user interface
- **Backend**: Flask (Python) for server-side logic
- **External Services**: OpenAI API for content generation
- **Asynchronous Processing**: AsyncIO for non-blocking operations
- **PDF Generation**: ReportLab for creating downloadable PDFs


The application uses a queue-based system for managing progress updates and employs coroutines for efficient API interactions.


## Prerequisites


- Python 3.10 or higher
- pip (Python package manager)
- OpenAI API key
- Docker (optional, for containerized deployment)
- Git (for version control and installation)


## Installation


1. Clone the repository:
   ```
   git clone https://github.com/yourusername/BookAI.git
   cd BookAI
   ```


2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```


3. Install the async Flask extension:
   ```
   pip install 'flask[async]'
   ```


## Usage


1. Start the Flask application:
   ```
   python app.py
   ```


2. Open a web browser and navigate to `http://localhost:5151` (or the appropriate port if you've changed it).


3. Enter the required information in the web interface:
   - OpenAI API Key
   - Model (e.g., "gpt-3.5-turbo")
   - Topic
   - Target word count
   - Language


4. Click "Generate Book" to start the book generation process.


5. Monitor the progress in real-time.


6. Once the book is generated, you can view it in the browser or download it as a PDF.


## Docker Deployment


To deploy BookAI using Docker:


1. Build the Docker image:
   ```
   docker build -t bookai .
   ```


2. Run the Docker container:
   ```
   docker run -p 5000:5000 bookai
   ```

## Configuration


The application can be configured using environment variables or a `.env` file:


- `FLASK_APP`: Set to "app.py"
- `FLASK_ENV`: Set to "development" for debugging, "production" for live environments
- `FLASK_RUN_HOST`: Set to "0.0.0.0" to make the app accessible outside the container
- `FLASK_RUN_PORT`: Set to 5151 by default, can be changed as needed
- `OPENAI_API_KEY`: Your OpenAI API key
- `MAX_TOKENS_PER_REQUEST`: Maximum tokens per API request (default: 500)
- `RATE_LIMIT_REQUESTS`: Number of requests allowed per minute (default: 50)


## Usage


### Basic Usage


1. Start the Flask application:
   ```bash
   flask run
   ```


2. Open a web browser and navigate to `http://localhost:5151`.


3. Enter the required information in the web interface:
   - OpenAI API Key (if not set in environment variables)
   - Model (e.g., "gpt-3.5-turbo", "gpt-4")
   - Topic
   - Target word count
   - Language


4. Click "Generate Book" to start the book generation process.


5. Monitor the progress in real-time.


6. Once the book is generated, you can view it in the browser or download it as a PDF.


### Advanced Usage


#### Custom Chapter Structures


You can define custom chapter structures by modifying the `generate_chunk` function in `app.py`. For example, to create a book with an introduction, conclusion, and themed chapters:


```python
async def generate_chunk(api_key, model, topic, current_word_count, language, structure):
    if structure == "introduction":
        prompt = f"Write an introduction for a book about {topic} in {language}."
    elif structure == "conclusion":
        prompt = f"Write a conclusion for a book about {topic} in {language}."
    elif structure == "chapter":
        prompt = f"Write a chapter for a book about {topic} in {language}, focusing on a specific aspect or subtopic."
    # ... rest of the function
```


#### API Usage Optimization


To optimize API usage and manage costs, you can implement a token budget system:


```python
MAX_TOKENS = 100000  # Example token budget


async def generate_book(topic, target_word_count, language):
    total_tokens_used = 0
    while total_tokens_used < MAX_TOKENS and current_word_count < target_word_count:
        chunk, tokens_used = await generate_chunk(...)
        total_tokens_used += tokens_used
        # ... process chunk
    return book_content, total_tokens_used
```


## API Reference


BookAI exposes the following API endpoints:


- `GET /`: Serves the main page
- `POST /generate`: Initiates book generation
  - Parameters:
    - `api_key`: OpenAI API key
    - `model`: OpenAI model to use
    - `topic`: Book topic
    - `word_count`: Target word count
    - `language`: Book language
  - Returns: JSON with generated content and word count
- `GET /progress`: Server-sent events for progress updates
- `POST /download-pdf`: Generates and serves a PDF of the book
  - Parameters:
    - `content`: Book content
    - `title`: Book title
    - `language`: Book language
  - Returns: PDF file


## Docker Deployment


To deploy BookAI using Docker:


1. Build the Docker image:
   ```bash
   docker build -t bookai .
   ```


2. Run the Docker container:
   ```bash
   docker run -p 5151:5151 -e OPENAI_API_KEY=your_api_key bookai
   ```


3. Access the application at `http://localhost:5151`.


For production deployment, consider using Docker Compose with a reverse proxy like Nginx for improved security and performance.


## Development


### Project Structure


```
BookAI/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template for the web interface
├── static/
│   ├── css/
│   │   └── styles.css  # Custom CSS styles
│   └── js/
│       └── script.js   # Client-side JavaScript
├── tests/
│   ├── test_app.py     # Unit tests for app.py
│   └── test_api.py     # API integration tests
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
├── .env.example        # Example environment variables
└── README.md           # This file
```


### Adding New Features


To add new features to BookAI:


1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Implement your feature, adding any necessary routes to `app.py`
3. Update the HTML template and JavaScript as needed
4. Add appropriate tests in the `tests/` directory
5. Update this README with any new configuration or usage instructions
6. Create a pull request for review


### Testing


Run the test suite using pytest:


```bash
pytest tests/
```


For integration tests that require an OpenAI API key, set the `OPENAI_API_KEY` environment variable before running the tests.


## Performance Optimization


To optimize BookAI's performance:


1. Implement caching for frequently generated content using Redis or Memcached
2. Use a task queue like Celery for long-running book generation jobs
3. Optimize database queries if a database is added in future versions
4. Consider implementing server-side rendering for improved initial load times
5. Use a content delivery network (CDN) for serving static assets in production


## Troubleshooting


Common issues and their solutions:


1. **API Key Issues**: Ensure your OpenAI API key is correctly set in the `.env` file or passed as an environment variable.


2. **Rate Limiting**: If you encounter rate limiting errors, adjust the `RATE_LIMIT_REQUESTS` configuration or implement exponential backoff in the `generate_chunk` function.


3. **Memory Issues**: For very long books, you may need to implement streaming responses or break the generation into smaller batches.


4. **PDF Generation Fails**: Ensure all required fonts are installed in your environment, or use only web-safe fonts in the PDF generation process.


## Contributing


Contributions to BookAI are welcome! Please follow these steps:


1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request


Please ensure your code adheres to the project's coding standards and includes appropriate tests.


## License


[MIT License](LICENSE)


## Disclaimer


BookAI uses OpenAI's API. Ensure compliance with OpenAI's use-case policy and terms of service when using this application. The generated content may require review and editing for accuracy and appropriateness. Users are responsible for the content they generate and its use.
