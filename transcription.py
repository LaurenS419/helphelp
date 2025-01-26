from openai import OpenAI
import sys

def get_key():
    file = open("openai-key.txt", "r")
    key = file.read()
    file.close()
    return key


def get_trans(file_path):
    print(f"Processing the file at: {file_path}")

    client = OpenAI(api_key=get_key())

    audio_file= open("uploads/recording.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    return transcription.text




    