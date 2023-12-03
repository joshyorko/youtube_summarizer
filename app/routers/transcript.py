from fastapi import APIRouter, Depends, HTTPException
from ..models import TranscriptRequest, TranscriptResponse
from ..dependencies import get_current_user
from ..services.getyoutube import download_and_transcribe_youtube_audio

router = APIRouter()

@router.post("/transcript", response_model=TranscriptResponse)
async def get_transcript(request: TranscriptRequest, user=Depends(get_current_user)):
    try:
        transcript = download_and_transcribe_youtube_audio(request.url)
        return TranscriptResponse(transcript=transcript)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))