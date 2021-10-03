from app.categories.schemas import AddCategoryDTO, CategoryDTO
from sqlalchemy.orm.session import Session
from app.database.dbconfig import get_db
from fastapi import APIRouter
from fastapi.param_functions import Depends
from . import repository
router = APIRouter(tags=['categories'])

@router.get('/',response_model=CategoryDTO)
def get_categories(db: Session = Depends(get_db)):
  return repository.get_categories(db)

@router.post('/',response_model=CategoryDTO)
def add_category(add_category_dto: AddCategoryDTO,db: Session = Depends(get_db)):
  return repository.add_category(add_category_dto=add_category_dto,db=db)