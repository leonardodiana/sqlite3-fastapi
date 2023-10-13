from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from typing import Optional

class StructureCreate(BaseModel):
 id: int
 name: str


class InfoCreate(BaseModel):
 id:int
 region: str
 year: int
 presenze: int
 arrivi: int
 structure: int



app= FastAPI()

import sqlite3

def create_connection():
 connection = sqlite3.connect("db.sqlite3")
 return connection

def create_structure(structure: StructureCreate):
 connection = create_connection()
 cursor = connection.cursor()
 cursor.execute("INSERT INTO structure(id, name) VALUES (?,?)", (structure.id, structure.name))
 connection.commit()
 connection.close()

@app.post("/structure")
def create_structure_endpoint(structure : StructureCreate):
    structure_id = create_structure(structure)
    return {"id": structure_id, **structure.dict()}

def create_info(info: InfoCreate):
 connection = create_connection()
 cursor = connection.cursor()
 cursor.execute("INSERT INTO info(id, region, year, presenze, arrivi, structure) VALUES (?,?,?,?,?,?)", (info.id, info.region, info.year, info.presenze, info.arrivi, info.structure))
 connection.commit()
 connection.close()

@app.post("/info")
def create_info_endpoint(info : InfoCreate):
    info_id = create_info(info)
    return {"id": info_id, **info.dict()}


