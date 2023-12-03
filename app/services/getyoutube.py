import os
import logging
import whisper
from pytube import YouTube, exceptions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transcribe_audio_mp4(audio_file_path: str) -> str:
    """
    Transcribes the audio file using the Whisper model.

    Args:
        audio_file_path (str): The path to the audio file.

    Returns:
        str: The transcript of the audio.
    """
    try:
        model = whisper.load_model("tiny")
        result = model.transcribe(audio_file_path)
        transcript = result.get("text", "")
        with open("transcript.md", "w", encoding="utf-8") as f:
            f.write(f'Summarize the following transcript into bullet points: {audio_file_path}:\n{transcript}')
        return transcript
    except Exception as e:
        logger.error(f"Error in transcribing audio: {e}")
        raise

def download_and_transcribe_youtube_audio(url: str) -> str:
    """
    Downloads the audio from a YouTube video and transcribes it.

    Args:
        url (str): The YouTube URL.

    Returns:
        str: The transcript of the audio.
    """
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if not audio_stream:
            raise ValueError("No audio stream found")

        audio_file_path = audio_stream.download()
        logger.info(f"Downloaded audio file: {audio_file_path}")

        try:
            return transcribe_audio_mp4(audio_file_path)
        finally:
            if os.path.exists(audio_file_path):
                os.remove(audio_file_path)
                logger.info(f"Cleaned up audio file: {audio_file_path}")

    except exceptions.PytubeError as e:
        logger.error(f"Pytube error: {e}")
        raise
    except Exception as e:
        logger.error(f"General error during download and transcription: {e}")
        raise

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=dFJxwl-azEA'
    try:
        transcript = download_and_transcribe_youtube_audio(url)
        print(transcript)
    except Exception as e:
        print(f"Error: {e}")