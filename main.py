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

@app.get("/structure/{name}")
def read_structure_by_name_endpoint(name:str, q: str | None = None):
  return read_structure_by_name(name)

@app.get("/structure")
def read_all_structure_endpoint():
  return read_all_structures()

@app.get("/info")
def read_all_infos_endpoint():
   return read_all_infos()

@app.get("/info/{region}")
def info_by_region_endpoint(region: str, q: str | None = None):
  return read_info_by_region(region)

@app.get("/info/{year}")
def info_by_year_endpoint(year:int):
  return read_info_by_year(year)

@app.get("/join")
def info_join_structure_region_endpoint(id_structure:int, region:str, q: str | None = None):
  return read_info_by_structure_and_region(id_structure, region)

