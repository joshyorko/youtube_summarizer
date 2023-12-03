from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

# Insert your generated JWT token here
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X3VzZXIiLCJleHAiOjE3MDE2NDEyMjJ9.bb658srE1ef2D9ml-SlHbTDnqq7w_055s_HaqXDjM7c"

@patch('app.services.getyoutube.download_and_transcribe_youtube_audio')
def test_get_transcript(mock_download_transcribe):
    mock_download_transcribe.return_value = "This is a test transcript."
    headers = {"Authorization": f"Bearer {TEST_TOKEN}"}

    response = client.post(
        "/transcript",
        headers=headers,
        json={"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    )
    assert response.status_code == 200
    assert response.json() == {"transcript": "This is a test transcript."}

def test_get_transcript_invalid_url():
    headers = {"Authorization": f"Bearer {TEST_TOKEN}"}

    response = client.post(
        "/transcript",
        headers=headers,
        json={"url": "invalid_url"},
    )
    assert response.status_code == 422  # 422 Unprocessable Entity for invalid URL
