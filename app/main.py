
from app.categories import categories
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users import users
from .database.dbconfig import engine
from .database.models import Base

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router,prefix='/users')
app.include_router(categories.router,prefix='/users')

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

