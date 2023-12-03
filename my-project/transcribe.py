import whisper

def transcribe_audio_mp4(audio_file_path):
    """
    Transcribes the audio file using Whisper model and saves the transcript in a markdown file.

    Args:
        audio_file_path (str): The path to the audio file.

    Returns:
        str: A message indicating the path of the audio file and the transcript.

    Raises:
        KeyError: If the result does not contain the "text" key.
    """
    # Transcribe audio using Whisper
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file_path)
    try:
        transcript = result["text"]
        with open("transcript.md", "w", encoding="utf-8") as f:
            f.write(f'Summarize the following transcript into bullet points: {audio_file_path}: /n{transcript}')
    except KeyError as e:
        print(e)
    return

if __name__ == "__main__":
    transcribe_audio_mp4(input("Enter the path to the audio file: "))
    
