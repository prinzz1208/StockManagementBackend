from app.database.helpers import save
from app.database.dbconfig import get_db
from fastapi.param_functions import Depends
from .schemas import AddCategoryDTO
from app.database import models
from sqlalchemy.orm.session import Session
from datetime import date
def get_categories(db: Session = Depends(get_db)):
  return db.query(models.Category).all()

def add_category(add_category_dto: AddCategoryDTO,db: Session):
  category = models.Category(name=add_category_dto.name,count=add_category_dto.count,date_in=date.today())
  return save(db,category)
  # return db.query(models.Category)