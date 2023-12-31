from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from crud import *
from models import *
import numpy as np

app = FastAPI()


@app.post("/structure")
def create_structure_endpoint(structure: StructureCreate):
    structure_id = create_structure(structure)
    return {"id": structure_id, **structure.model_dump()}


@app.post("/info")
def create_info_endpoint(info: InfoCreate):
    info_id = create_info(info)
    return {"id": info_id, **info.model_dump()}


@app.get("/structure/{id}")
def read_structure_endpoint(id: int):
    return read_structure(id)


@app.get("/structure")
def read_all_structure_endpoint():
    return read_all_structures()

@app.get("/info")
def read_all_infos_endpoint():
    return read_all_infos()
# @app.get("/info")
# def read_all_infos_endpoint(year: int | None = None, region: str | None = None):
#     if(year!=None):
#       return read_info_by_year(year)
#     if(region!=None):
#         return read_info_by_region(region)
#     if(region==None and year==None):
#         return read_all_infos()

@app.get("/info/{year}")
def info_by_year_endpoint(year: int):
    return read_info_by_year(year)

@app.get("/info-region/{region}")
def info_by_region_endpoint(region: str, q: str | None = None):
    return read_info_by_region(region)

@app.get("/join")
def info_join_structure_region_endpoint(id_structure: int, region: str, q: str | None = None):
    return read_info_by_structure_and_region(id_structure, region)

@app.get("/join/{column}")
def info_join_filtered_by_column_endpoint(id_structure: int, region: str, column:str):
    result=read_info_by_structure_and_region(id_structure, region)
    result_filtered=[]
    for x in result:
        if(column=="arrivi"):
            result_filtered.append(x["arrivi"])
        elif(column=="partenze"):
            result_filtered.append(x["partenze"])
    return result_filtered

@app.get("/mean-for_region_by_structure")
def mean_for_region_by_strcture_endpoint(id_structure: int, region: str, column:str):
    result=read_info_by_structure_and_region(id_structure, region)
    result_filtered=[]
    for x in result:
        if(column=="arrivi"):
            result_filtered.append(x["arrivi"])
        elif(column=="partenze"):
            result_filtered.append(x["partenze"])
    return np.mean(result_filtered)


@app.get("/mean-for_region")
def mean_for_region_endpoint(region: str, column:str):
    result=read_info_by_region(region)
    result_filtered=[]
    for x in result:
        if(column=="arrivi"):
            result_filtered.append(x["arrivi"])
        elif(column=="partenze"):
            result_filtered.append(x["partenze"])
    return np.mean(result_filtered)