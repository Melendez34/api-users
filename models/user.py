"""Users Model Table Database"""
from sqlalchemy import Column, Integer, String
from config.database import Base


class UserTableModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    im = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
