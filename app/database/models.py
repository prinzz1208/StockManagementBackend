from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from .dbconfig import Base
from sqlalchemy import Column

class User(Base):
  __tablename__ = "user"
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  email = Column(String)
  password = Column(String)


class Category(Base):
  __tablename__ = 'category'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  count = Column(Integer)
  date_in = Column(DateTime)

class Product(Base):
  __tablename__ = 'product'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  specifications = Column(String)
  category_id = Column(Integer, ForeignKey('category.id'))


class Store(Base):
  __tablename__ = 'store'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  address = Column(String)
  phone = Column(String)
  user_id = Column(Integer, ForeignKey('user.id'))