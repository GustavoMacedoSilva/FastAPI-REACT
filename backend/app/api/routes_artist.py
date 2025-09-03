from fastapi import APIRouter
from typing import Optional

router = APIRouter()
@router.get('/artist')#apenas pegamos 10 artistas
def index(limit =10,most_famous:bool=False, sort: Optional[str]= None):
    if most_famous:
        return {'data': f'{limit} most famous artist from the db'}
    else:
        return {'data': f'{limit} artist from the db'}

@router.get('/artist/{artist_id}')
def showArtist(artist_id: int):
    return {'data': artist_id}