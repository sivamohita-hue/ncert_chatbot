from fastapi import FastAPI
from pydantic import BaseModel
from translator import normalize_query
from search import fetch_answer

app = FastAPI()

class Question(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(q: Question):

    original_question = q.question

    # Normalize Tanglish / Hinglish
    normalized_question = normalize_query(original_question)

    # Fetch answer from web
    answer = fetch_answer(normalized_question)

    return {
        "question": original_question,
        "normalized_question": normalized_question,
        "answer": answer
    }
