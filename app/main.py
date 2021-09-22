
from fastapi import  FastAPI
from app.users import users
from .database.dbconfig import engine
from .database.models import Base

app = FastAPI()

app.include_router(users.router,prefix='/users')

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

