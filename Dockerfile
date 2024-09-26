# Use the official Python image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    libsndfile1 \
    libatomic1 \
    curl && \ 
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
    chmod a+rx /usr/local/bin/yt-dlp


# Create a working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py .
COPY requirements.txt .

# Command to run the script
CMD ["python", "app.py"]
