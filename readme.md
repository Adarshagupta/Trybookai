# BookAI


BookAI is a Flask-based web application that generates books using OpenAI's language models. It allows users to specify a topic, target word count, language, and other parameters to create custom books. The application also provides functionality to download the generated book as a PDF.


## Features


- Generate books on any topic using OpenAI's language models
- Support for multiple languages
- Real-time progress tracking
- PDF download option
- Asynchronous generation for improved performance


## Prerequisites


- Python 3.10 or higher
- Docker (optional, for containerized deployment)


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


3. Access the application at `http://localhost:5000`.


## Project Structure


- `app.py`: Main Flask application file
- `templates/index.html`: HTML template for the web interface
- `requirements.txt`: List of Python dependencies
- `Dockerfile`: Instructions for building the Docker image


## Configuration


You can modify the following environment variables in the Dockerfile or when running the container:


- `FLASK_APP`: Set to "app.py"
- `FLASK_RUN_HOST`: Set to "0.0.0.0" to make the app accessible outside the container
- `FLASK_RUN_PORT`: Set to 5000 by default, can be changed as needed


## API Endpoints


- `/`: Main page
- `/generate`: POST endpoint for book generation
- `/progress`: Server-sent events endpoint for progress updates
- `/download-pdf`: POST endpoint for PDF generation and download


## Error Handling


BookAI includes basic error handling for API requests and PDF generation. Check the server logs for detailed error messages in case of issues.


## Contributing


Contributions to BookAI are welcome! Please feel free to submit a Pull Request.


## License


[MIT License](LICENSE)


## Disclaimer


BookAI uses OpenAI's API. Make sure you comply with OpenAI's use-case policy and terms of service when using this application.
