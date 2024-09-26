# Vosk Speech-to-Text Transcription from YouTube Video

## Overview

This project uses Vosk, an open-source speech recognition toolkit, to transcribe the audio from a YouTube video into text. The video is downloaded, the audio is extracted, and the content is transcribed into a text file.

## Prerequisites

- Docker and Docker Compose installed on your machine.

- Download a Vosk model from [Vosk Models](https://alphacephei.com/vosk/models) and place the extracted "model" directory inside this project folder.

## Getting Started

### 1. Clone the Repository

Clone the project repository to your local machine.

### 2. Place Vosk Model

Download and extract a Vosk model from the [Vosk Models page](https://alphacephei.com/vosk/models). Place the extracted "model" folder in the root of this project directory.

### 3. Run the Docker Container Using Docker Compose

Navigate to the project directory and run:

```bash
docker-compose up
```

The transcription will be saved in output/output.txt in the project folder.

# Changing the YouTube Video

To transcribe a different YouTube video, update the command section in docker-compose.yml with the desired video URL.

# Notes
Make sure the model folder exists and is correctly downloaded.

The output/output.txt file will contain the transcription of the audio from the provided YouTube video.

# License
MIT