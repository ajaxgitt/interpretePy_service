import tempfile
import os
import subprocess


def variables(nombre_funcion,problema, casos_de_prueba ):
    verificar_code = """
def verificar_respuestas(funcion, casos):
    try:
        pruebas_pasadas = 0
        for _, caso in enumerate(casos):
            entrada = caso["entrada"].split(",")[0]
            entrada2 = caso["entrada"].split(",")[1]
            try:
                salida_esperada = int(caso["salida_esperada"])  
            except ValueError:
                salida_esperada = caso["salida_esperada"] 
            
            salida_obtenida = funcion(int(entrada), int(entrada2))
            if salida_obtenida == salida_esperada:
                pruebas_pasadas += 1
    except ValueError :
        pruebas_pasadas = 0
        for _, caso in enumerate(casos):
            entrada = caso["entrada"].split(",")[0]
            entrada2 = caso["entrada"].split(",")[1]
            salida_esperada = caso["salida_esperada"]
            salida_obtenida = funcion(entrada, entrada2)
            
            if salida_obtenida == salida_esperada:
                pruebas_pasadas += 1
    return pruebas_pasadas

"""
    return f"{problema}\n{verificar_code}\nprint(verificar_respuestas({nombre_funcion}, {casos_de_prueba}))"


# Crear archivo tempooral
def run_codigo(codigo):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
        temp_file.write(codigo.encode())
        if any(keyword in codigo and keyword not in ["import os", "import subprocess"] for keyword in ["import", "eval", "exec", "open", "sys"]):
            return 20
        temp_file_path = temp_file.name
    try:
        result = subprocess.run(['python', temp_file_path], timeout=5, text=True, capture_output=True)
        if result.returncode != 0:
            if "NameError" in result.stderr:
                return 100  
        
        if result.returncode == 0:
            print(int(result.stdout.strip()[-1]))
            return int(result.stdout.strip()[-1])
        else:
            return result.returncode
    except subprocess.TimeoutExpired:
        return 10
    except Exception as e:
        print(e)
        return str(e)  
    except NameError as e:
    # Capturamos y mostramos el error
        print(f"Ocurrió un error de tipo NameError: {e}")
   
    finally:
        os.remove(temp_file_path)




