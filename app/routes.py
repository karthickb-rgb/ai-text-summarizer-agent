from fastapi import APIRouter
from app.service import summarize_text

router = APIRouter()

@router.post("/summarize")
def summarize(data: dict):
    text = data.get("text")
    result = summarize_text(text)
    return {"summary": result}
