from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    try:
        # Save file and process content
        content = await file.read()
        # Here we'll add document processing logic
        return {"filename": file.filename, "status": "success"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/generate-questions")
async def generate_questions():
    # Sample questions (will be AI-generated later)
    questions = [
        {"id": 1, "question": "What is your projected revenue for year 1?"},
        {"id": 2, "question": "What are your main revenue streams?"},
        {"id": 3, "question": "What is your initial investment requirement?"}
    ]
    return questions

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)