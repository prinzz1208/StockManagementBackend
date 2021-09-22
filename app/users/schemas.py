
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserBase(BaseModel):
    id: int
    email: str
    firstName: str
    lastName: str

class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
      orm_mode = True

class UserWithToken(Token):
    email: str
    
    class Config:
      orm_mode = True




class TokenData(BaseModel):
    username: Optional[str] = None
