
from pydantic import BaseModel
from typing import List
from datetime import datetime


class TestCaseShema(BaseModel):
    entrada: str
    salida_esperada: str

class CodeShema(BaseModel):
    nombre_funcion:str
    codigo : str
    casos_de_prueba : List[TestCaseShema]