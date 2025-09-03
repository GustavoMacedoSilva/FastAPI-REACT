from fastapi import APIRouter, Depends
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db



router = APIRouter()

@router.get('/user/{user_username}/listenedAlbums')
def listenedAlbums(user_username: str):
    return {'data': {'Album 1', 'Album 2'}}

@router.get('/user/{user_username}/reviews')
def userReviews(user_username):
    return {'data': {'review1': "blablabla", 'review2': "blablablba"}}


@router.post('/user')
def createUser(request_user:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(nome=request_user.nome, username=request_user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user