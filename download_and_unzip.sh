#!/bin/bash

# Define the URL and the output zip file name
URL="https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip"
ZIP_FILE="vosk-model-en-us-0.42-gigaspeech.zip"
TARGET_DIR="model"

# Download the zip file
echo "Downloading $ZIP_FILE..."
curl -O $URL

# Create the target directory if it doesn't exist
mkdir -p $TARGET_DIR

# Unzip the downloaded file to the target directory
echo "Unzipping $ZIP_FILE to $TARGET_DIR..."
unzip $ZIP_FILE -d $TARGET_DIR

# Optionally, remove the zip file after extraction
# rm $ZIP_FILE

echo "Download and extraction complete."