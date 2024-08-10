# 📚 BookAI: AI-Powered Book Generation 🤖

BookAI is a revolutionary web application that harnesses the power of artificial intelligence to generate high-quality, professional books in minutes. Our cutting-edge AI technology empowers authors, content creators, and businesses to streamline their writing process and produce market-ready books with unprecedented speed and efficiency.

![BookAI](https://raw.githubusercontent.com/Adarshagupta/BookAI/main/book.png)

[![GitHub license](https://img.shields.io/github/license/Adarshagupta/BookAI.svg)](https://github.com/Adarshagupta/BookAI/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/release/Adarshagupta/BookAI.svg)](https://github.com/Adarshagupta/BookAI/releases/)
[![GitHub stars](https://img.shields.io/github/stars/Adarshagupta/BookAI.svg)](https://github.com/Adarshagupta/BookAI/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Adarshagupta/BookAI.svg)](https://github.com/Adarshagupta/BookAI/issues/)

## 🌟 Features

* 📖 Book Generation
* 🌍 Multiple Language Support
* 🗣️ Text-to-Speech Functionality
* 📄 PDF Download
* 📊 Analytics Dashboard

## 🚀 Usage

### 📚 Generating a Book

1. Access the application at the provided URL.
2. Fill out the form with the following details:
   * 🤖 Model: Choose between GPT-3.5 Turbo, GPT-4o Mini, or GPT-4o Mini (2024-07-18)
   * 🌐 Language: Select English, Hindi (Experimental), or Spanish
   * 📝 Book Topic: Enter the main subject of your book
   * 📏 Target Word Count: Specify the desired length of your book
3. Click "Generate Book" to start the process.
4. Wait for the generation to complete. Progress will be displayed in real-time.

### 🗣️ Text-to-Speech

1. Once the book is generated, use the play/pause button to start or stop the text-to-speech feature.
2. Select a voice from the dropdown menu to change the speaking voice.

### 📥 Downloading the Book

1. After generation, click the "Download Your Book" button.
2. The book will be downloaded as a PDF file.

### 📊 Analytics Dashboard

After book generation, an analytics dashboard will display:

* 📊 Word Count
* 📈 Readability Score
* 🏷️ Genre Classification
* 😊 Sentiment Analysis

## 💻 Local Setup

### Requirements

* Python 3.7+
* pip (Python package manager)
* OpenAI API key

### Installation Steps

1. ```bash
   git clone https://github.com/your-repo/ai-book-generator.git
   cd ai-book-generator```
   

### Set up virtual environment
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

### Install dependencies
```
pip install -r requirements.txt
```

### Set OpenAI API key
```
export OPENAI_API_KEY=your_api_key_here
```

### Run the application4
```
python app.py
```

# Open a web browser and navigate to http://localhost:5000

### Docker Setup
### Requirements:
#### * Docker installed on your system
#### * OpenAI API key

### Build Docker image
```
docker build -t ai-book-generator .
```

### Run Docker container
```
docker run -p 5000:5000 -e OPENAI_API_KEY=your_api_key_here ai-book-generator
```

#### Access the application by opening a web browser and navigating to http://localhost:5000

Note: Make sure to replace your\_api\_key\_here with your actual OpenAI API key when running the container.

🛠️ Technical Details
---------------------

### Frontend

*   HTML5, CSS3 (Tailwind CSS), JavaScript (jQuery)
    
*   Responsive design for various screen sizes
    
*   Uses server-sent events for real-time progress updates
    

### Backend

*   Python Flask server
    
*   Asynchronous book generation using aiohttp
    
*   OpenAI API integration for content generation
    
*   ReportLab for PDF creation
    

### API Endpoints

*   /generate (POST): Initiates book generation
    
*   /progress (GET): Provides real-time generation progress
    
*   /download-pdf (POST): Creates and serves the PDF file
    

⚠️ Known Limitations
--------------------

*   Hindi language support is experimental and may have inconsistencies
    
*   Generation time increases with higher word counts
    
*   API rate limits may affect generation speed for longer books
    

🔧 Troubleshooting
------------------

If you encounter issues:

1.  Ensure you have a stable internet connection
    
2.  Check if the OpenAI API is operational
    
3.  For persistent problems, contact support with error details displayed on the page
    

🔮 Future Enhancements
----------------------

*   Support for more languages
    
*   Integration with additional AI models
    
*   Enhanced analytics and content optimization features
    
*   Audio book download functionality (coming soon)
    

🖼️ Demo Images
---------------

Show ImageShow ImageShow Image

🏆 Featured on ProductHunt
--------------------------

[![BookAI - AI-powered book generation in minutes | Product Hunt](https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=123456&theme=light)](https://www.producthunt.com/posts/bookai?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-bookai)

🙌 Contributors
---------------

[![](https://contrib.rocks/image?repo=Adarshagupta/BookAI)](https://github.com/Adarshagupta/BookAI/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

📄 License
----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML
