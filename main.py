from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from db"}
    return {"data": f"{limit} blogs from db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"commets": id}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"}
