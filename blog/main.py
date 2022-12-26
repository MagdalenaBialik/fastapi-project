from fastapi import FastAPI
from blog import schemas

app = FastAPI()


@app.post("/blog")
def create(request: schemas.Blog):
    return request
