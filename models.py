from fastapi import FastAPI
from pydantic import BaseModel

class InfoCreate(BaseModel):
 id: int 
 region: str
 year: int
 presenze: int
 arrivi: int
 structure: int

class StructureCreate(BaseModel):
 id: int
 name: str
 infos: list[InfoCreate]