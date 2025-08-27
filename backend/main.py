from fastapi import FastAPI
from typing import Optional

app = FastAPI()
# uvicorn main:app --reload
@app.get('/artist')#apenas pegamos 10 artistas
def index(limit =10,most_famous:bool=False, sort: Optional[str]= None):
    if most_famous:
        return {'data': f'{limit} most famous artist from the db'}
    else:
        return {'data': f'{limit} artist from the db'}

@app.get('/artist/{artist_id}')
def showArtist(artist_id: int):
    return {'data': artist_id}

@app.get('/user/{user_username}/listenedAlbums')
def listenedAlbums(user_username: str):
    return {'data': {'Album 1', 'Album 2'}}

@app.get('/user/{user_username}/reviews')
def userReviews(user_username):
    return {'data': {'review1': "blablabla", 'review2': "blablablba"}}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)