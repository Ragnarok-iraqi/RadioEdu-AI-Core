from fastapi import FastAPI

app = FastAPI(title="RadioEdu AI Backend")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "RadioEdu AI backend running"}
