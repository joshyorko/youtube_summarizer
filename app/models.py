from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class TranscriptRequest(BaseModel):
    url: HttpUrl = Field(..., description="The YouTube video URL to transcribe.")

class TranscriptResponse(BaseModel):
    transcript: str = Field(..., description="The transcribed text of the YouTube video.")
    summary: Optional[str] = Field(None, description="An optional summary of the transcript.")
