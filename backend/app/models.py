from database import base
from sqlalchemy import Column, Integer, String

class User(base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String)
    username = Column(String, index=True, unique=True)
    