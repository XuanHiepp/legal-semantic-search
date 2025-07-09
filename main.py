from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"


# 1. FastAPI Initialization
app = FastAPI(
    title="Legal Dense Search API",
    description="RESTful API: Semantic search Điều luật dùng PhoBERT + Qdrant",
    version="1.0"
)


# 2. Load model PhoBERT
model = SentenceTransformer(
    "VoVanPhuc/sup-SimCSE-VietNamese-phobert-base",
    device='cpu'
)


# 3. Connect Qdrant Cloud
def load_env(env_file):
    with open(env_file) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key] = value


load_env('.env')

qdrant_url = os.getenv("QDRANT_URL")
qdrant_key = os.getenv("QDRANT_API_KEY")
qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_key,
)


# 4. Request schema
class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    title: str


# 5. Endpoint /search
@app.post("/search", response_model=List[SearchResult])
def search(req: SearchRequest):
    user_query = req.query

    # Encode query
    query_vec = model.encode(user_query, normalize_embeddings=True)

    # Dense search
    hits = qdrant_client.query_points(
        collection_name="laws_collection",
        query=query_vec.tolist(),
        limit=20,
        with_payload=True
    ).points

    seen_titles = set()
    results = []

    for hit in hits:
        payload = hit.payload
        title = payload.get("title", "").strip()

        # If saw the title, skip it.
        if title in seen_titles:
            continue

        seen_titles.add(title)

        results.append(SearchResult(
            id=payload.get("id"),
            title=title,
            score=round(hit.score, 4)
        ))

    # Get top 5 hits
    results = results[:5]

    return results
