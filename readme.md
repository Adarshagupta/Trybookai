# 📚 BookAI: AI-Powered Book Generation 🤖

BookAI is a revolutionary web application that harnesses the power of artificial intelligence to generate high-quality, professional books in minutes. Our cutting-edge AI technology empowers authors, content creators, and businesses to streamline their writing process and produce market-ready books with unprecedented speed and efficiency.

![BookAI](https://raw.githubusercontent.com/adarshagupta/trybookai/main/book.png)

[![GitHub license](https://img.shields.io/github/license/adarshagupta/trybookai.svg)](https://github.com/adarshagupta/trybookai/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/release/adarshagupta/trybookai.svg)](https://github.com/adarshagupta/trybookai/releases/)
[![GitHub stars](https://img.shields.io/github/stars/adarshagupta/trybookai.svg)](https://github.com/adarshagupta/trybookai/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/adarshagupta/trybookai.svg)](https://github.com/adarshagupta/trybookai/issues/)

AI-Powered Book Generation and Management System
================================================

Table of Contents
-----------------

1.  [Overview](#overview)
    
2.  [Features](#features)
    
3.  [Technologies Used](#technologies-used)
    
4.  [System Architecture](#system-architecture)
    
5.  [API Endpoints](#api-endpoints)
    
6.  [Authentication and Security](#authentication-and-security)
    
7.  [Database](#database)
    
8.  [PDF Generation](#pdf-generation)
    
9.  [Email Notifications](#email-notifications)
    
10.  [Deployment](#deployment)
    

1\. Overview
------------

This project is an AI-powered book generation and management system that allows users to create, download, and manage AI-generated books. It incorporates various AI models, authentication systems, and database management to provide a comprehensive solution for automated book creation.

2\. Features
------------

*   AI-powered book generation using OpenAI and Together AI models
    
*   Multi-language support for book generation
    
*   PDF creation and management
    
*   User authentication and registration with OTP verification
    
*   API key generation for programmatic access
    
*   Email notifications for user actions
    
*   Progress tracking for book generation
    
*   Saved PDF management and download functionality
    
*   Web-based user interface for book generation and management
    
*   RESTful API for programmatic access to book generation features
    

3\. Technologies Used
---------------------

*   **Backend**: Python, Flask
    
*   **Database**: SQLite
    
*   **Authentication**: Firebase Authentication
    
*   **AI Models**: OpenAI API, Together AI API
    
*   **PDF Generation**: ReportLab
    
*   **Email**: Flask-Mail
    
*   **Frontend**: HTML, CSS, JavaScript (assumed, not shown in the provided code)
    
*   **API Documentation**: Not specified, but could be implemented using Swagger/OpenAPI
    
*   **Logging**: Python's built-in logging module
    
*   **Environment Variables**: python-dotenv
    
*   **Asynchronous Programming**: asyncio, aiohttp
    

4\. System Architecture
-----------------------

The system follows a modular architecture with the following components:

*   Web Server (Flask)
    
*   Authentication Service (Firebase)
    
*   Database Service (SQLite)
    
*   AI Integration Services (OpenAI, Together AI)
    
*   PDF Generation Service
    
*   Email Notification Service
    
*   API Key Management Service
    

5\. API Endpoints
-----------------

*   /: Home page
    
*   /about: About page
    
*   /fr: French version of the home page
    
*   /jobs: Jobs page
    
*   /playground: Interactive playground
    
*   /generate (POST): Generate book content
    
*   /progress: Server-Sent Events for progress tracking
    
*   /download-pdf (POST): Generate and download PDF
    
*   /save-pdf (POST): Save generated PDF
    
*   /get-saved-pdfs (GET): Retrieve saved PDFs
    
*   /download-saved-pdf/ (GET): Download a specific saved PDF
    
*   /generate-api-key (POST): Generate API key for a user
    
*   /api/generate-book (POST): API endpoint for book generation
    
*   /api: API documentation page
    
*   /login (POST): User login
    
*   /verify-login (POST): Verify login OTP
    
*   /register (POST): User registration
    
*   /verify-registration (POST): Verify registration OTP
    
*   /auth: Authentication page
    

6\. Authentication and Security
-------------------------------

*   Firebase Authentication for user management
    
*   OTP (One-Time Password) verification for login and registration
    
*   Session management using Flask sessions
    
*   API key authentication for programmatic access
    
*   HTTPS recommended for production deployment (not implemented in the provided code)
    

7\. Database
------------

*   SQLite database for storing PDF metadata and API keys
    
*   Tables:
    
    *   pdfs: Stores information about generated PDFs
        
    *   api\_keys: Stores API keys associated with users
        

8\. PDF Generation
------------------

*   Uses ReportLab library to create PDF documents
    
*   Supports custom styling and formatting
    
*   Generates PDFs from AI-generated content
    

9\. Email Notifications
-----------------------

*   Uses Flask-Mail for sending emails
    
*   Sends notifications for user registration and login
    
*   Sends OTP for user verification
    

10\. Deployment
---------------

*   The application is designed to run on a Flask development server
    
*   For production, it's recommended to use a production-grade WSGI server like Gunicorn
    
*   Environment variables should be properly set in production for sensitive information
    

Additional Notes
----------------

*   The system uses asynchronous programming for handling concurrent book generation requests
    
*   Progress tracking is implemented using Server-Sent Events
    
*   The code includes error handling and logging for better debugging and monitoring
    
*   The system is designed to handle rate limiting and API usage tracking
    

This documentation provides an overview of the main components and features of the AI-powered book generation and management system. For more detailed information on each component or feature, additional documentation may be necessary.

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

[![](https://contrib.rocks/image?repo=adarshagupta/trybookai)](https://github.com/adarshagupta/trybookai/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

📄 License
----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML
