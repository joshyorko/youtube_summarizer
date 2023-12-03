# YouTube Transcript Service

This service is a FastAPI microservice that takes a YouTube URL and returns the transcript of the video.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Docker (optional)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/youtube_transcript_service.git
```

2. Navigate to the project directory:

```bash
cd youtube_transcript_service
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload
```

The API documentation will be available at `http://localhost:8000/docs`.

## Running the tests

To run the tests, execute:

```bash
pytest
```

## Deployment

To build a Docker image of the application, run:

```bash
docker build -t youtube_transcript_service .
```

To start a container, run:

```bash
docker run -p 8000:8000 youtube_transcript_service
```

## API Endpoints

- `POST /transcript`: Takes a YouTube URL and returns the transcript of the video.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.