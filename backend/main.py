from fastapi import FastAPI
from app.api.routes_user import router as user_router
from app.api.routes_artist import router as artist_router
from app.api.routes_albums import router as album_router
from app import schemas, models
from app.database import engine

app = FastAPI(
    title="SocialJAM",
    description="API to socialize based on your music taste",
)
# uvicorn main:app --reload
models.base.metadata.create_all(engine)
app.include_router(user_router)
app.include_router(artist_router)
app.include_router(album_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)