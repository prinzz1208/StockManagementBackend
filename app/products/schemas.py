from datetime import date, datetime
from pydantic.main import BaseModel


class AddProductDTO(BaseModel):
  name: str
  specifications: str
  category_id: int

class ProductDTO(BaseModel):
  name: str
  specifications: str
  class Config:
         orm_mode=True
