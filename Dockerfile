# Use the official Python image from the Docker Hub
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file first
COPY requirements.txt .

# Install build dependencies and create a virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Start a new stage for a smaller final image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]