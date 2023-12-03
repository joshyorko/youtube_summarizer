from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.generate_token import create_test_token

client = TestClient(app)

# Insert your generated JWT token here
TEST_TOKEN = create_test_token()

@patch('app.routers.transcript.get_current_user')
@patch('app.services.getyoutube.download_and_transcribe_youtube_audio')
def test_get_transcript(mock_get_current_user, mock_download_transcribe):
    mock_get_current_user.return_value = {'user': 'mock_user'}  # Adjust this to match your user model
    mock_download_transcribe.return_value = "This is a test transcript."
    headers = {"Authorization": f"Bearer {TEST_TOKEN}"}

    response = client.post(
        "/transcript",
        headers=headers,
        json={"url": "https://www.youtube.com/watch?v=dFJxwl-azEA"},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert "transcript" in response_data  # Check if 'transcript' key exists in response


def test_get_transcript_invalid_url():
    headers = {"Authorization": f"Bearer {TEST_TOKEN}"}

    response = client.post(
        "/transcript",
        headers=headers,
        json={"url": "invalid_url"},
    )
    assert response.status_code == 422  # 422 Unprocessable Entity for invalid URL