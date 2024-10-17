

casos_de_prueba = [
{'entrada': '10,2', 'salida_esperada': '5'},
{'entrada': '9,3', 'salida_esperada': '3'},
{'entrada': '7,0', 'salida_esperada': 'Error: Division por cero'},
{'entrada': '15,5', 'salida_esperada': '3'},
{'entrada': '-6,2', 'salida_esperada': '-3'},
]

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
                

        if pruebas_pasadas == 0 :
            return 6
    except ValueError :
        pruebas_pasadas = 0
        for _, caso in enumerate(casos):
            entrada = caso["entrada"].split(",")[0]
            entrada2 = caso["entrada"].split(",")[1]
            salida_esperada = caso["salida_esperada"]
            
            salida_obtenida = funcion(entrada, entrada2)
            
            if salida_obtenida == salida_esperada:
                pruebas_pasadas += 1
                

        if pruebas_pasadas == 0 :
            return 6
        
    return pruebas_pasadas



def divide_dos_numeros(a,b):
    if b ==0:
        return "Error: Division por cero"
    return a // b


print(verificar_respuestas(divide_dos_numeros, casos_de_prueba))

