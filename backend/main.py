from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.request_models import VideoRequest
from services.rag_pipeline import generate_notes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Video Notes Generator API running"}

@app.post("/generate-notes")
def generate_video_notes(request: VideoRequest):

    notes = generate_notes(request.url)

    return {"notes": notes}