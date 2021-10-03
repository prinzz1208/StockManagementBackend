from app.categories.schemas import AddproductDTO, productDTO
from sqlalchemy.orm.session import Session
from app.database.dbconfig import get_db
from fastapi import APIRouter
from fastapi.param_functions import Depends

from app.products.schemas import AddProductDTO, ProductDTO
from . import repository
router = APIRouter(tags=['products'])

@router.get('/{category_id}')
def get_products(category_id:int, db: Session = Depends(get_db)):
  return repository.get_products(category_id=category_id,db=db)

@router.post('/{category_id}',response_model=ProductDTO)
def add_product(category_id:int, add_product_dto: AddProductDTO, db: Session = Depends(get_db)):
  return repository.add_product(category_id, add_product_dto=add_product_dto,db=db)