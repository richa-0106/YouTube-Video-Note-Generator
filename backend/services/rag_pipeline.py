from services.downloader import download_audio
from services.transcriber import transcribe_audio
from services.summarizer import summarize


def generate_notes(url):

    print("Downloading video...")
    audio = download_audio(url)

    print("Transcribing audio...")
    transcript = transcribe_audio(audio)

    print("Generating notes...")
    notes = summarize(transcript)

    return notes