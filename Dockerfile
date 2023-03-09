FROM python:3.9-slim-buster

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80 5000

# Copy application files
COPY database.py .
COPY app app
COPY . .

# Define environment variable
ENV FLASK_APP=app/__init__.py

# Set environment variables for database connection
ENV DB_HOST db
ENV DB_NAME mydatabase
ENV DB_USER myuser
ENV DB_PASS mypassword

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

