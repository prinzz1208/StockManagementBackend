from sqlalchemy.orm.session import Session

from app.database import models
from app.database.helpers import save
from app.products.schemas import AddProductDTO


def get_products(category_id,db:Session):
  return db.query(models.Product).filter(category_id=category_id).all()

def add_product(add_product_dto: AddProductDTO,db: Session):
  product = models.product(name=add_product_dto.name,count=add_product_dto.count,date_in=date.today())
  return save(db,product)
  # return db.query(models.Category)