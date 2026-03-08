from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from translator import normalize_query
from search import fetch_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TEST ROUTE
@app.get("/")
def test():
    return {"message": "Backend is working"}

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Question):

    original_question = q.question
    normalized_question = normalize_query(original_question)
    answer = fetch_answer(normalized_question)

    return {
        "question": original_question,
        "normalized_question": normalized_question,
        "answer": answer
    }
