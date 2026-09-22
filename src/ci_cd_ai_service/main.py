import os

from fastapi import FastAPI

from ci_cd_ai_service.calculator import add

app = FastAPI()


app_env = os.getenv("APP_ENV", "development")


@app.get("/")
def root():
    return {"message": "AI Service is running"}


@app.get("/add")
def calculate(a: int, b: int):
    return {"result": add(a, b)}


@app.get("/environment")
def environment():
    return {"environment": app_env}


@app.get("/health")
def health():
    return {"status": "healthy"}