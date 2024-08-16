# 📚 AI Book Generator Documentation 📚

## 📖 Table of Contents 📖

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
    - [Generating a Book](#generating-a-book)
    - [Downloading a PDF](#downloading-a-pdf)
    - [Managing API Keys](#managing-api-keys)
    - [User Authentication](#user-authentication)
    - [Generating Images](#generating-images)
7. [API Documentation](#api-documentation)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)
10. [License](#license)

## 🚀 Introduction 🚀

The AI Book Generator is a powerful web application that leverages AI models from OpenAI and Together to generate detailed books on a wide range of topics. Users can customize their book's content, language, and length, and then download the final product as a PDF. The application also includes features for API key management, user authentication via Firebase, and image generation using the Hugging Face API.

![Book Image](https://raw.githubusercontent.com/Adarshagupta/BookAI/main/book2.png?token=GHSAT0AAAAAACWCFWSSAQBCSFRZANHDBDYQZV7CQNA)

## ✨ Features ✨

- **Book Generation**: Utilize AI models to generate comprehensive books on any topic.
- **Language Customization**: Choose the language for your book's content.
- **Word Count Control**: Specify the target word count for your book.
- **PDF Download**: Save and download your generated book as a PDF.
- **API Key Management**: Generate and manage API keys for secure access to the book generation API.
- **User Authentication**: Secure user registration and login using Firebase.
- **Image Generation**: Generate images based on text prompts using the Hugging Face API.

## 🛠️ Technologies Used 🛠️

- **Flask**: A lightweight WSGI web application framework in Python.
- **OpenAI API**: Provides access to advanced AI models for text generation.
- **Together API**: Another AI service for text generation.
- **Hugging Face API**: Used for generating images from text prompts.
- **Firebase**: For secure user authentication and management.
- **SQLite**: A lightweight, serverless database used for storing PDF metadata and API keys.
- **ReportLab**: A library for creating PDFs from dynamic data.
- **aiohttp**: An asynchronous HTTP client/server for Python.
- **asyncio**: Python library for writing single-threaded concurrent code using coroutines.

## 📦 Installation 📦

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/ai-book-generator.git
    cd ai-book-generator
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```
    OPENAI_API_KEY=your_openai_api_key
    TOGETHER_API_KEY=your_together_api_key
    GETIMG_API_KEY=your_getimg_api_key
    ```

5. **Initialize the database**:
    ```bash
    python
    >>> from app import init_db
    >>> init_db()
    >>> exit()
    ```

6. **Run the application**:
    ```bash
    flask run
    ```

## ⚙️ Configuration ⚙️

The application uses environment variables for configuration. Ensure that the following variables are set in your `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `TOGETHER_API_KEY`: Your Together API key.
- `GETIMG_API_KEY`: Your Hugging Face API key.

## 📚 Usage 📚

### Generating a Book

1. **Access the web application**:
    Open your browser and navigate to `http://localhost:5000`.

2. **Navigate to the playground**:
    Click on the "Playground" link in the navigation menu.

3. **Select your preferences**:
    - Choose the AI model (OpenAI or Together).
    - Enter the topic for your book.
    - Select the language.
    - Specify the target word count.

4. **Generate the book**:
    Click on the "Generate Book" button. The progress of the book generation will be displayed.

### Downloading a PDF

1. **Once the book is generated**:
    The content will be displayed on the screen.

2. **Download the PDF**:
    Click on the "Download PDF" button to save the book as a PDF file.

### Managing API Keys

1. **Navigate to the API page**:
    Click on the "API" link in the navigation menu.

2. **Generate a new API key**:
    Click on the "Generate API Key" button. Your new API key will be displayed.

3. **View and manage your API keys**:
    Your existing API keys will be listed on the page. You can revoke or regenerate keys as needed.

### User Authentication

1. **Register a new account**:
    - Navigate to the "Auth" page.
    - Click on the "Register" button.
    - Enter your email, password, and phone number.
    - Click on the "Register" button to create your account.

2. **Log in to your account**:
    - Navigate to the "Auth" page.
    - Click on the "Login" button.
    - Enter your email and password.
    - Click on the "Login" button to access your account.

### Generating Images

1. **Navigate to the image generation page**:
    Click on the "Generate Image" link in the navigation menu.

2. **Enter a text prompt**:
    Type a description of the image you want to generate.

3. **Generate the image**:
    Click on the "Generate Image" button. The generated image will be displayed on the screen.

## 📜 API Documentation 📜

The API allows for programmatic access to the book generation functionality. Refer to the [API Documentation](#api-documentation) for detailed information on available endpoints and how to use them.

### Endpoints

- **POST /generate-book**: Generate a book using the specified AI model, topic, language, and word count.
- **POST /generate-api-key**: Generate a new API key for accessing the API.
- **POST /generate-image**: Generate an image based on a text prompt.

### Request Format

- **Generate Book**:
    ```json
    {
        "api": "openai",
        "model": "gpt-3.5-turbo",
        "topic": "Artificial Intelligence",
        "language": "English",
        "word_count": 5000
    }
    ```

- **Generate API Key**:
    ```json
    {}
    ```

- **Generate Image**:
    ```json
    {
        "prompt": "A futuristic cityscape at night"
    }
    ```

### Response Format

- **Generate Book**:
    ```json
    {
        "content": "Book content here...",
        "word_count": 5000
    }
    ```

- **Generate API Key**:
    ```json
    {
        "api_key": "your_new_api_key"
    }
    ```

- **Generate Image**:
    ```json
    {
        "output": "data:image/png;base64,image_data_here"
    }
    ```

## 🔧 Troubleshooting 🔧

- **API Key Issues**: Ensure that your API keys are correctly set in the `.env` file and are valid.
- **Database Issues**: If you encounter issues with the database, ensure that the SQLite database is correctly initialized and accessible.
- **Authentication Issues**: If you have trouble logging in or registering, ensure that your Firebase credentials are correctly configured.

## 🤝 Contributing 🤝

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## 📄 License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
