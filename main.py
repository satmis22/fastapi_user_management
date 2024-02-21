from fastapi import FastAPI
from database import engine
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}