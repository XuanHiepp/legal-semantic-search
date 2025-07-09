# Installation Guide and Usage Instructions
A simple RESTful API for semantic search of Vietnamese legal documents using FastAPI, Sentence-BERT, and Qdrant.

## Features
- Search Vietnamese legal articles with semantic understanding.
- Uses PhoBERT embeddings (via Sentence-BERT).
- Vector storage & search powered by Qdrant.
- Endpoint /search returns relevant articles (title and content).

## Tech Stack
- FastAPI — Python web API framework

- Sentence-BERT — Vietnamese PhoBERT model for embeddings

- Qdrant — Vector database for similarity search

- Docker — Containerized deployment

## Usage.
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload

# Or with Docker Compose
docker-compose up --build
```

## Example Query.
POST /search
{
  "query": "NLĐ bị sa thải có được trả lương hay không?"
}