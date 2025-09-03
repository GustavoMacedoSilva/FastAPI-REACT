from .database import base
from sqlalchemy import Column, Integer, String

class User(base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=True)
    username = Column(String, index=True, unique=True)
    favorite_artist = Column(String, nullable=True)