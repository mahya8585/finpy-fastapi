from typing import Union, Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello!"}


@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}


@app.get("/user/")
def get_user_pathparam(name: str, lang: Union[str, None] = None):
    return {"name": name, "lang": lang}


@app.get("/user/{id}/details")
def get_user_details(id: int, keyword: str):
    return {"id": id, "keyword": keyword}


data = [
    {"id": 1, "name": "Datha"},
    {"id": 2, "name": "Fidelity"},
    {"id": 3, "name": "Rani"},
]


class User(BaseModel):
    id: int
    name: str


class ShowUser(BaseModel):
    name: str


@app.post("/user", response_model=List[ShowUser])
def add_user(request: User):
    data.append({"id": request.id, "name": request.name})
    return data
