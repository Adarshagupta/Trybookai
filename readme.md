AI Book Generator Documentation

===============================

The AI Book Generator is a web application that allows users to generate books on any topic using artificial intelligence. It leverages OpenAI's language models to create coherent and engaging book content based on user input.

Features

--------

*   Book Generation

*   Multiple Language Support

*   Text-to-Speech Functionality

*   PDF Download

*   Analytics Dashboard

Usage

-----

### Generating a Book

1\.  Access the application at the provided URL.

2\.  Fill out the form with the following details:

    *   Model: Choose between GPT-3.5 Turbo, GPT-4o Mini, or GPT-4o Mini (2024-07-18)

    *   Language: Select English, Hindi (Experimental), or Spanish

    *   Book Topic: Enter the main subject of your book

    *   Target Word Count: Specify the desired length of your book

3\.  Click "Generate Book" to start the process.

4\.  Wait for the generation to complete. Progress will be displayed in real-time.

### Text-to-Speech

1\.  Once the book is generated, use the play/pause button to start or stop the text-to-speech feature.

2\.  Select a voice from the dropdown menu to change the speaking voice.

### Downloading the Book

1\.  After generation, click the "Download Your Book" button.

2\.  The book will be downloaded as a PDF file.

### Analytics Dashboard

After book generation, an analytics dashboard will display:

*   Word Count

*   Readability Score

*   Genre Classification

*   Sentiment Analysis

Local Setup

-----------

### Requirements

*   Python 3.7+

*   pip (Python package manager)

*   OpenAI API key

### Installation Steps

1\.  git clone https://github.com/your-repo/ai-book-generator.gitcd ai-book-generator

2\.  python -m venv venvsource venv/bin/activate # On Windows use \`venv\\Scripts\\activate\`

3\.  pip install -r requirements.txt

4\.  OPENAI\_API\_KEY=your\_api\_key\_here

5\.  python app.py

6\.  Open a web browser and navigate to http://localhost:5000

Docker Setup

------------

### Requirements

*   Docker installed on your system

*   OpenAI API key

### Dockerfile

The application includes a Dockerfile with the following content:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Use the official Python image from the Docker Hub  FROM python:3.10-slim  # Set the working directory  WORKDIR /app  # Copy the requirements file  COPY requirements.txt .  # Install any dependencies  RUN pip install --no-cache-dir -r requirements.txt  # Copy the rest of the application code  COPY . .  # Set environment variables  ENV FLASK_APP=app.py  ENV FLASK_RUN_HOST=0.0.0.0  # Expose the port the app runs on  EXPOSE 5000  # Run the Flask app  CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]   `

### Building and Running the Docker Container

1\.  docker build -t ai-book-generator .

2\.  docker run -p 5000:5000 -e OPENAI\_API\_KEY=your\_api\_key\_here ai-book-generator

3\.  Access the application by opening a web browser and navigating to http://localhost:5000

Note: Make sure to replace your\_api\_key\_here with your actual OpenAI API key when running the container.

Technical Details

-----------------

### Frontend

*   HTML5, CSS3 (Tailwind CSS), JavaScript (jQuery)

*   Responsive design for various screen sizes

*   Uses server-sent events for real-time progress updates

### Backend

*   Python Flask server

*   Asynchronous book generation using aiohttp

*   OpenAI API integration for content generation

*   ReportLab for PDF creation

### API Endpoints

*   /generate (POST): Initiates book generation

*   /progress (GET): Provides real-time generation progress

*   /download-pdf (POST): Creates and serves the PDF file

Known Limitations

-----------------

*   Hindi language support is experimental and may have inconsistencies

*   Generation time increases with higher word counts

*   API rate limits may affect generation speed for longer books

Troubleshooting

---------------

If you encounter issues:

1\.  Ensure you have a stable internet connection

2\.  Check if the OpenAI API is operational

3\.  For persistent problems, contact support with error details displayed on the page

Future Enhancements

-------------------

*   Support for more languages

*   Integration with additional AI models

*   Enhanced analytics and content optimization features

*   Audio book download functionality (coming soon)
