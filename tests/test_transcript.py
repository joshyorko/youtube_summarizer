from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@patch('app.services.getyoutube.download_and_transcribe_youtube_audio')
def test_get_transcript(mock_download_transcribe):
    mock_download_transcribe.return_value = "This is a test transcript."

    response = client.post(
        "/transcript",
        json={"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    )
    assert response.status_code == 200
    assert response.json() == {"transcript": "This is a test transcript."}

def test_get_transcript_invalid_url():
    response = client.post(
        "/transcript",
        json={"url": "invalid_url"},
    )
    assert response.status_code == 422  # 422 Unprocessable Entity for invalid URL

# Add more tests for different scenarios like unauthenticated access, network errors, etc.
