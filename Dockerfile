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

# Copy application files
COPY database.py .

# Set environment variables for database connection
ENV DB_HOST db
ENV DB_NAME mydatabase
ENV DB_USER myuser
ENV DB_PASS mypassword

# Run the script
CMD [ "python", "./database.py" ]
