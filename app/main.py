from fastapi import FastAPI
from .database.dbconfig import engine
from .database.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}