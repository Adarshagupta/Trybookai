# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the app runs on
EXPOSE 5000

# Debug: List files in the working directory
RUN ls -la /app

# Debug: Print FLASK_APP variable
RUN echo $FLASK_APP

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
