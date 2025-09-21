from fastapi import FastAPI, status, HTTPException
from typing import Optional, Annotated
import random

from fastapi.params import Query

app = FastAPI()

names_list = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Maryam"},
    {"id": 3, "name": "Arousha"},
    {"id": 4, "name": "Aziz"},
    {"id": 5, "name": "Zahra"},
    {"id": 6, "name": "Ali"},
    {"id": 7, "name": "Ali"},
    {"id": 8, "name": "Ali"},
]


@app.get("/")
def root():
    return {"message": "Hello World!"}


# /names (GET(RETRIEVE), POST(CREATE))
# @app.get("/names")
# def retrieve_name_list():
#     return names_list

# @app.get("/names")
# def retrieve_name_list(q: str | None = None):
#     if q:
#         # [Operation, Iteration, Condition]
#         return [item for item in names_list if item["name"] == q]
#     return names_list


@app.get("/names")
# def retrieve_name_list(q: Optional[str] = None):
def retrieve_name_list(q: Annotated[str | None, Query(max_length=50)] = None):
    if q:
        # [Operation, Iteration, Condition]
        return [item for item in names_list if item["name"] == q]
    return names_list


@app.post("/names", status_code=status.HTTP_201_CREATED)
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
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found!")


@app.put("/names/{name_id}", status_code=status.HTTP_200_OK)
def update_name_detail(name_id: int, name: str):
    for item in names_list:
        if item["id"] == name_id:
            item["name"] = name
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found!")


@app.delete("/names/{name_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_name(name_id: int):
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return {"detail": "Object removed successfully!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found!")
