"""Users Model Table Database"""
from sqlalchemy import Column, Integer, String
from config.database import Base

class User_Table_Model(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key= True)
  name = Column(String)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  im = Column(String)
