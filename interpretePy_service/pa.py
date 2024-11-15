
import tempfile
import os
import subprocess





def variables(nombre_funcion,problema, casos_de_prueba ):

    verificar_code = """
def verificar_respuestas(funcion, casos):
    pruebas_pasadas = 0
    for i, caso in enumerate(casos):
        entrada = caso["entrada"].split(",")[0]
        entrada2 = caso["entrada"].split(",")[1]
        salida_esperada = int(caso["salida_esperada"])  
        
        salida_obtenida = funcion(int(entrada), int(entrada2))
        
        if salida_obtenida == salida_esperada:
            pruebas_pasadas += 1

    if pruebas_pasadas == 0 :
        return 6
    return pruebas_pasadas
"""
    return f"{problema}\n{verificar_code}\nprint(verificar_respuestas({nombre_funcion}, {casos_de_prueba}))"






# Crear un archivo temporal
def run_codigo(codigo):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
        temp_file.write(codigo.encode())
        if any(keyword in codigo and keyword not in ["import os", "import subprocess"] for keyword in ["import", "eval", "exec", "open", "sys"]):
            return "CM"
        temp_file_path = temp_file.name
    try:
        result = subprocess.run(['python', temp_file_path], timeout=5, text=True, capture_output=True)
        print(result)
        if result.returncode == 0:
            print(int(result.stdout.strip()[-1]))
            return int(result.stdout.strip()[-1])
        else:
            return result.returncode
    except subprocess.TimeoutExpired:
        return "El código ha sido detenido por exceder el tiempo límite"
    except Exception as e:  # Captura cualquier otra excepción
        print(e)
        return str(e)  
    
    
    finally:
        os.remove(temp_file_path)




