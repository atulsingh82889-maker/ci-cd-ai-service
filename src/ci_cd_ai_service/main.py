from fastapi import FastAPI

from ci_cd_ai_service.calculator import add

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Service is running"}


@app.get("/add")
def calculate(a: int, b: int):
    return {"result": add(a, b)}
