from fastapi import APIRouter
from ..schemas import User

router = APIRouter()

@router.get('/user/{user_username}/listenedAlbums')
def listenedAlbums(user_username: str):
    return {'data': {'Album 1', 'Album 2'}}

@router.get('/user/{user_username}/reviews')
def userReviews(user_username):
    return {'data': {'review1': "blablabla", 'review2': "blablablba"}}


@router.post('/user')
def createUser(request_user:User):
    return {'data': 'User created!', 'data2': f'Welcome {request_user.username}'}