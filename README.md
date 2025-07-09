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
### 4.1. Load streamlit tool.
The project is developed using the FastAPI tool. To execute the project:
```bash
docker pull xuanhiepp/legal-search-api:latest
docker run -p 8000:8000 xuanhiepp/legal-search-api:latest
```
Since the port is mapped as 8501:8501 in docker-compose.yml, you can open your browser and access the application at:
http://localhost:8000/docs or http://127.0.0.1:8000/docs

## Example Query.
```
POST /search
{
  "query": "NLĐ bị sa thải có được trả lương hay không?"
}
```