from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from models import *
import json

app = FastAPI()

import sqlite3


def create_connection():
    connection = sqlite3.connect("db.sqlite3")
    return connection



# CREATE


def create_structure(structure: StructureCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO structure(id, name) VALUES (?,?)", (structure.id, structure.name)
    )
    connection.commit()
    connection.close()


def create_info(info: InfoCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO info(id, region, year, presenze, arrivi, structure) VALUES (?,?,?,?,?,?)",
        (info.id, info.region, info.year, info.presenze, info.arrivi, info.structure),
    )
    connection.commit()
    connection.close()


# READ


def read_structure(id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM structure where id = ?", (id,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result


def read_all_structures():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM structure")
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def read_all_infos():
    connection = create_connection()
    cursor = connection.cursor()
    result =cursor.execute("SELECT * FROM info")
    result = cursor.fetchall()
    column_names = [d[0] for d in cursor.description]
    for row in result:
        info = dict(zip(column_names, row))
        final = json.dumps(info)
    connection.commit()
    connection.close()
    return final


def read_info_by_year(year: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM info where year= ?", (year,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def read_info_by_region(region: str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM info where region= ?", (region,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def read_info_by_structure_and_region(id_structure: int, region: str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM structure as s INNER JOIN info as i on s.id=i.structure WHERE s.id=? and i.region = ?",
        (
            id_structure,
            region,
        ),
    )
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

# def search_info(year:int=None, region:str=None):
#     #Build query
#     query="SELECT * FROM info"
#     conditions=[]
#     if year is not None:
#         conditions.append("year = ?")
#     if region is not None:
#         conditions.append("region = ?")
#     if conditions:
#         query += " WHERE " + " AND ".join(conditions)
#     connection = create_connection()
#     cursor = connection.cursor()
#     cursor.execute(query,(year,))
#     result = cursor.fetchall()
#     connection.commit()
#     connection.close()
#     return result


print(read_all_infos())
