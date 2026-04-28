from app.utils import call_openai

def summarize_text(text: str):
    prompt = f"Summarize this text:\n{text}"
    return call_openai(prompt)
