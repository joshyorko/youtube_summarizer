from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import transcript

app = FastAPI(
    title="YouTube Transcript Service",
    description="A service to transcribe YouTube videos.",
    version="1.0.0"
)

# CORS Middleware (adjust origins according to your needs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(transcript.router)



# Optionally, you can add custom exception handlers here

# Example endpoint for health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}
