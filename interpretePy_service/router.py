from fastapi import APIRouter, HTTPException
from .schemas import TestCaseShema , CodeShema
from .services import run_codigo , variables


interprete = APIRouter()


        
@interprete.get("/api")
def saludo():
    return "hola mundo"

@interprete.post("/api/code")
def revisar_codigo(code:CodeShema):
    """funcion para probar el codigo del user 
    se necesita de tres argumentos nombre de la funcion, el codigo del user y los casos de prueba de la db"""
    nombre_funcion = code.nombre_funcion
    problema = code.codigo
    casos_de_prueba = [x.dict() for x in code.casos_de_prueba]
    caso = str(casos_de_prueba)
    
    
    
    var = variables(nombre_funcion=nombre_funcion,problema=problema ,casos_de_prueba=caso)
    analisis = run_codigo(var)
    if analisis ==  "CM":
        # return HTTPException(status_code=400, detail="Código malicioso detectado")
        return {"status": "bad", "message": "Código malicioso detectado"}
    elif analisis == 5:
        return {"status": "success", "message": "Pasó todas las pruebas"}
    elif 2 <= analisis <=4 or analisis == 6:
        return {"status": "info", "message": "Tu algoritmo no superó las pruebas de Sherlock. Por favor, revisa el codigo."}

    
    else:
        return {
            "status": "error",
            "message": (
                "Error en tiempo de ejecución. Posibles causas:\n"
                "- Error de tipo\n"
                "- Falta de indentación\n"
                "- Símbolos faltantes\n"
                "- Errores de sintaxis"
            )
        }

        
    
  
