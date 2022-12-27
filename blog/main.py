from fastapi import FastAPI
from blog import schemas, models
from blog.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("/blog")
def create(request: schemas.Blog, db):
    return db
