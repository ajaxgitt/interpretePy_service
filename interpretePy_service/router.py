from fastapi import APIRouter, HTTPException
from .schemas import  CodeShema 
from .services import run_codigo , variables
from .services_d2 import run_codigo_d2, variables_d2
from .services_d3 import run_codigo_d3, variables_d3


interprete = APIRouter()

@interprete.post("/api/code/1")
def revisar_codigo(code:CodeShema):
    """funcion para probar el codigo del user se necesita de tres argumentos nombre de la funcion, el codigo del user y los casos de prueba de la db"""
    match run_codigo(variables(code.nombre_funcion,code.codigo,str([x.dict() for x in code.casos_de_prueba]))):
        case 0|1|2|3|4:
            return {"status": "info", "message": "Tu algoritmo no superó las  pruebas. Por favor, revisa el codigo."}
        case 5:
            return {"status": "success", "message": "Paso todas las pruebas"}
        case 10:
            return {"status": "loop", "message": "El programa ha sido detenido por exceder el tiempo límite, posible causa loop infinito"}
        case 20:
            return {"status": "bad", "message": "Codigo malicioso detectado"}
        case  100:
            return {"status": "name_error", "message": "Nombre de funcion incorrecto!"}
        case _:
            return {
            "status": "error",
            "message": (
                "Error en tiempo de ejecución. Posibles causas:\n"
                "- Error de tipo\n"
                "- Falta de indentación\n"
                "- Símbolos faltantes\n"
            )
        }
            
            
     
    
@interprete.post('/api/code/2')
def revisar_codigo_dificultad_2(code:CodeShema):
    match run_codigo_d2(variables_d2(code.nombre_funcion,code.codigo,str([x.dict() for x in code.casos_de_prueba]))):
        case 0|1|2|3|4:
            return {"status": "info", "message": "Tu algoritmo no superó las  pruebas. Por favor, revisa el codigo."}
        case 5:
            return {"status": "success", "message": "Paso todas las pruebas"}
        case 10:
            return {"status": "loop", "message": "El programa ha sido detenido por exceder el tiempo límite, posible causa loop infinito"}
        case 20:
            return {"status": "bad", "message": "Codigo malicioso detectado"}
        case  100:
            return {"status": "name_error", "message": "Nombre de funcion incorrecto!"}
        case _:
            return {
            "status": "error",
            "message": (
                "Error en tiempo de ejecución. Posibles causas:\n"
                "- Error de tipo\n"
                "- Falta de indentación\n"
                "- Símbolos faltantes\n"
            )
        }
            

import ast


@interprete.post('/api/code/3')
def revisar_codigo_dificultad_3(code:CodeShema):
    lista_caso = str([x.dict() for x in code.casos_de_prueba])
    match run_codigo_d3(variables_d3(code.nombre_funcion,code.codigo,lista_caso)):
        case 0|1|2|3|4:
            return {"status": "info", "message": "Tu algoritmo no supero las  pruebas. Por favor, revisa el codigo."}
        case 5:
            return {"status": "success", "message": "Paso todas las pruebas"}
        case 10:
            return {"status": "loop", "message": "El programa ha sido detenido por exceder el tiempo límite, posible causa loop infinito"}
        case 20:
            return {"status": "bad", "message": "Codigo malicioso detectado"}
        case  100:
            return {"status": "name_error", "message": "Nombre de funcion incorrecto!"}
        case _:
            return {
            "status": "error",
            "message": (
                "Error en tiempo de ejecución. Posibles causas:\n"
                "- Error de tipo\n"
                "- Falta de indentación\n"
                "- Símbolos faltantes\n"
            )
        }
    
    