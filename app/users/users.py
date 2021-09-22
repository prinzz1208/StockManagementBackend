from datetime import timedelta

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from ..database.dbconfig import get_db
from ..utils import constants, hash
from . import repository
from .schemas import Token, UserWithToken, UserLogin

router = APIRouter(tags=['users'])

@router.post("/login",response_model=Token)
async def login_for_access_token(form_data: UserLogin,db: Session = Depends(get_db)):

    user = repository.authenticate_user(db, form_data.email, form_data.password)

    if not user:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Incorrect username or password",

            headers={"WWW-Authenticate": "Bearer"},

        )

    access_token = hash.get_access_token(repository.get_user_by_email(db,form_data.email))
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup",response_model=UserWithToken)
def signup(user: UserLogin, db: Session = Depends(get_db),):
    db_user = repository.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    newUser = repository.create_user(db=db, user=user)
    access_token = hash.get_access_token(user)
    return {"email": newUser.email,"access_token": access_token, "token_type": "bearer"}
