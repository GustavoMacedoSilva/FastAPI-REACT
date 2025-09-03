from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    username: str
    nome: Optional[str] = None
    username: str
    
class Artist(BaseModel):
    nome: str
    music_genre: List[str]