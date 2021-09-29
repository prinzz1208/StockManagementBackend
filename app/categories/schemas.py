from datetime import date, datetime
from pydantic.main import BaseModel


class AddCategoryDTO(BaseModel):
  name: str
  count: int

class CategoryDTO(BaseModel):
  name: str
  count: int
  date_in: datetime
  class Config:
         orm_mode=True
