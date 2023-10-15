from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from crud import *
from models import *


app= FastAPI()

@app.post("/structure")
def create_structure_endpoint(structure : StructureCreate):
    structure_id = create_structure(structure)
    return {"id": structure_id, **structure.model_dump()}

@app.post("/info")
def create_info_endpoint(info : InfoCreate):
    info_id = create_info(info)
    return {"id": info_id, **info.model_dump()}


@app.get("/structure/{id}")
def read_structure_endpoint(id:int):
  return read_structure(id)


@app.get("/structure")
def read_all_structure_endpoint():
  return read_all_structures()



