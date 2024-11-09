import tempfile
import os
import subprocess


def variables_d3(nombre_funcion,problema, casos_de_prueba):
    verificar_code = """
import ast


def verificar_respuestas(funcion, casos):
    pruebas_pasadas = 0
    for _, caso in enumerate(casos):
        entrada_lista = ast.literal_eval(caso['entrada'])
        try:
            salida_esperada = caso["salida_esperada"]
            salida_obtenida = funcion(entrada_lista)
            print(salida_obtenida,salida_esperada)
            
            if str(salida_obtenida) == salida_esperada:
                pruebas_pasadas += 1
        except TypeError as e:
            salida_esperada = caso["salida_esperada"]
            salida_obtenida = funcion(entrada_lista[0],entrada_lista[1])
            if str(salida_obtenida) == str(salida_esperada):
                pruebas_pasadas += 1
    print('pruebas_pasadas', pruebas_pasadas)
    return pruebas_pasadas

"""
    return f"{problema}\n{verificar_code}\nprint(verificar_respuestas({nombre_funcion}, {casos_de_prueba}))"

def run_codigo_d3(codigo):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
        temp_file.write(codigo.encode())
        if any(keyword in codigo and keyword not in ["import os", "import subprocess"] for keyword in ["exec", "open", "sys"]):
            return 20
        temp_file_path = temp_file.name
    try:
        result = subprocess.run(['python', temp_file_path], timeout=5, text=True, capture_output=True)
        print(result)
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



