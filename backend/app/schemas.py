from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    username: str
    name: Optional[str] = None
    
class Artist(BaseModel):
    name: str
    music_genre: List[str]