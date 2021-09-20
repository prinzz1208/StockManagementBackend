from sqlalchemy.sql.sqltypes import Integer, String
from .dbconfig import Base
from sqlalchemy import Column
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True,index=True)
  firstName = Column(String)
  lastName = Column(String)
  email = Column(String)
  password = Column(String)