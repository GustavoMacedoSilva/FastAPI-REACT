from fastapi import FastAPI

app = FastAPI()
# uvicorn main:app --reload
@app.get('/')
def index():
    return {'data': {'name': 'Gugu'}}

@app.get('/about')
def about():
    return {'data': 'About Page'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)