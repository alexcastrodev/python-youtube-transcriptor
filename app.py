import wave
import json
import os
import sys
from vosk import Model, KaldiRecognizer
import subprocess

# Use yt-dlp to download YouTube video as audio
def download_audio_from_youtube(url, output_audio):
    # Check if the audio file already exists
    if not os.path.exists(output_audio):
        subprocess.call([
            'yt-dlp',
            '--extract-audio',
            '--audio-format', 'wav',
            '--output', 'audio.%(ext)s',
            url
        ])
        # Rename the downloaded file to match output_audio
        os.rename('audio.wav', output_audio)
    else:
        print(f"{output_audio} already exists, skipping download.")

# Transcribe audio to text
def transcribe_audio(model_path, audio_path, output_text_file):
    model = Model(model_path)
    
    with wave.open(audio_path, "rb") as wf:
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        
        with open(output_text_file, 'w') as f:
            while True:
                data = wf.readframes(800)  # Reduced frame size for more frequent output
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    text = result['text']
                    print(text)  # Print transcribed text to the console
                    f.write(text + "\n")
            # Final result
            final_result = json.loads(rec.FinalResult())
            final_text = final_result['text']
            print(final_text)  # Print final transcribed text to the console
            f.write(final_text + "\n")

if __name__ == "__main__":
    # Check if URL is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python app.py <YouTube URL>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    audio_file = "audio.wav"
    output_text_file = "./output/output.txt"
    
    # Download Vosk model (ensure you have the "model" directory in the same folder)
    model_path = "model"
    
    print("Downloading and extracting audio...")
    download_audio_from_youtube(youtube_url, audio_file)
    
    print("Transcribing audio to text...")
    transcribe_audio(model_path, audio_file, output_text_file)
    
    print(f"Transcription complete. Check the {output_text_file} file.")
