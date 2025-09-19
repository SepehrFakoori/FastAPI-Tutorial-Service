from fastapi import FastAPI
import random

app = FastAPI()

names_list = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Maryam"},
    {"id": 3, "name": "Arousha"},
    {"id": 4, "name": "Aziz"},
    {"id": 5, "name": "Zahra"},
]


@app.get("/")
def root():
    return {"message": "Hello World!"}


# /names (GET(RETRIEVE), POST(CREATE))
@app.get("/names")
def retrieve_name_list():
    return names_list


@app.post("/names")
def create_name(name: str):
    name_obj = {"id": random.randint(6, 100), "name": name}
    names_list.append(name_obj)
    return name_obj


# /names/:id (GET(RETRIEVE), PUT/PATCH(UPDATE), DELETE)
@app.get("/names/{name_id}")
def retrieve_name_detail(name_id: int):
    for name in names_list:
        if name["id"] == name_id:
            return name
    return {"detail": "Object not found!"}
