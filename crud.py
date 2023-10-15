from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from models import *

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

def create_info(info: InfoCreate):
 connection = create_connection()
 cursor = connection.cursor()
 cursor.execute("INSERT INTO info(id, region, year, presenze, arrivi, structure) VALUES (?,?,?,?,?,?)", (info.id, info.region, info.year, info.presenze, info.arrivi, info.structure))
 connection.commit()
 connection.close()


def read_structure(id:int):
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


