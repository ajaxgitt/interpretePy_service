from services import run_codigo, variables
import tempfile
import os
import subprocess

code = """
# Aquí podrás probar tu código antes de enviarlo
def suma_dos_numeros(a, b):
    return a + b
    

casos_de_prueba = [
    {'entrada': '2, 5', 'salida_esperada': '7'},
    {'entrada': '10, 15', 'salida_esperada': '25'},
    {'entrada': '0, 0', 'salida_esperada': '0'},
    {'entrada': '-1, 1', 'salida_esperada': '0'},
    {'entrada': '3, 4', 'salida_esperada': '7'}
]

def verificar_respuestas(funcion, casos):
    pruebas_pasadas = 0
    for i, caso in enumerate(casos):
        entrada = caso["entrada"].split(",")[0]
        entrada2 = caso["entrada"].split(",")[1]
        salida_esperada = int(caso["salida_esperada"])  
        
        salida_obtenida = funcion(int(entrada), int(entrada2))
        
        if salida_obtenida == salida_esperada:
            pruebas_pasadas += 1

    return pruebas_pasadas

# Al final del bloque, devolver el resultado
print("holi")
resultado = verificar_respuestas(suma_dos_numeros, casos_de_prueba)
print(resultado)  # Aquí se imprime el resultado de verificar_respuestas
"""

# Crear un archivo temporal
def run_codigo(code):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
        temp_file.write(code.encode())
        temp_file_path = temp_file.name
    try:
        result = subprocess.run(['python', temp_file_path], timeout=5, text=True, capture_output=True)
        return result.stdout.strip()[-1]

    except subprocess.TimeoutExpired:
        return "El código ha sido detenido por exceder el tiempo límite"
    finally:
        os.remove(temp_file_path)

# Ejecutar el código y capturar el resultado
ress = run_codigo(code=code)
print(ress) 
