import ast





# casos_de_prueba = [
#     {'entrada': '2', 'salida_esperada': 'es primo'},
#     {'entrada': '10', 'salida_esperada': 'No es primo'},
#     {'entrada': '17', 'salida_esperada': 'es primo'},
#     {'entrada': '25', 'salida_esperada': 'No es primo'},
#     {'entrada': '97', 'salida_esperada': 'es primo'}
# ]

# casos_de_prueba = [
#     {'entrada': '0', 'salida_esperada': '1'},
#     {'entrada': '5', 'salida_esperada': '120'},
#     {'entrada': '3', 'salida_esperada': '6'},
#     {'entrada': '5', 'salida_esperada': '120'},
#     {'entrada': '10', 'salida_esperada': '3628800'}
# ]


#entrada str
#entrada int

#salida str
#salida str

# casos_de_prueba = [
#     {'entrada': 'radar', 'salida_esperada': 'True'},
#     {'entrada': 'osod', 'salida_esperada': 'False'},
#     {'entrada': 'oso', 'salida_esperada': 'True'},
#     {'entrada': 'anilina', 'salida_esperada': 'True'},
#     {'entrada': '97', 'salida_esperada': 'False'}
# ]

# casos_de_prueba = [
#     {'entrada': 'radar', 'salida_esperada': '2'},
#     {'entrada': 'sod', 'salida_esperada': '1'},
#     {'entrada': 'oso', 'salida_esperada': '2'},
#     {'entrada': 'murcielago', 'salida_esperada': '5'},
#     {'entrada': '97', 'salida_esperada': '0'}
# ]


# casos_de_prueba = [
#     {'entrada': 'hola', 'salida_esperada': 'aloh'},
#     {'entrada': 'python', 'salida_esperada': 'nohtyp'},
#     {'entrada': 'radar', 'salida_esperada': 'radar'},
#     {'entrada': '12345', 'salida_esperada': '54321'},
#     {'entrada': 'oro', 'salida_esperada': 'oro'}
# ]

# casos_de_prueba = [
#     {'entrada': '[1,2,3,4]', 'salida_esperada': '[2, 4]'},
#     {'entrada': '[2]', 'salida_esperada': '[2]'},
#     {'entrada': '[1]', 'salida_esperada': '[]'},
#     {'entrada': '[1,2,3,4,5,6,7]', 'salida_esperada': '[2, 4, 6]'},
#     {'entrada': '[0,1,2]', 'salida_esperada': '[0, 2]'}
# ]
# casos_de_prueba = [
#     {'entrada': '[1,2,-3,4]', 'salida_esperada': '4'},
#     {'entrada': '[]', 'salida_esperada': '0'},
#     {'entrada': '[1]', 'salida_esperada': '1'},
#     {'entrada': '[1,2 ,3,4,5,6,7]', 'salida_esperada': '7'},
#     {'entrada': '[0,1,2]', 'salida_esperada': '3'}
# ]


# casos_de_prueba = [
#     {'entrada': '[1, 2, 2, 3, 4]', 'salida_esperada': '4'},
#     {'entrada': '[1, 1, 1, 1]', 'salida_esperada': '1'},
#     {'entrada': '[7, 8, 9, 7, 10]', 'salida_esperada': '4'},
#     {'entrada': '[]', 'salida_esperada': '0'},
#     {'entrada': '[3, 3, 3, 4, 5]', 'salida_esperada': '3'}
# ]

# casos_de_prueba = [
#     {'entrada': '[1, 2, 3, 4]', 'salida_esperada': '10'},
#     {'entrada': '[10, -2, 3]', 'salida_esperada': '11'},
#     {'entrada': '[]', 'salida_esperada': '0'},
#     {'entrada': '[5]', 'salida_esperada': '5'},
#     {'entrada': '[1, 1, 1, 1]', 'salida_esperada': '4'}
# ]

# casos_de_prueba = [
#     {'entrada': '[1, 2, 3, 4]', 'salida_esperada': '4'},
#     {'entrada': '[-1, -2, -3]', 'salida_esperada': '-1'},
#     {'entrada': '[10,9,8]', 'salida_esperada': '10'},
#     {'entrada': '[]', 'salida_esperada': 'Lista vacia'},
#     {'entrada': '[7]', 'salida_esperada': '7'}
# ]

casos_de_prueba = [
    {'entrada': '[1, 2, 3, 1, 4, 1], 1', 'salida_esperada': '3'},
    {'entrada': '[10, 20, 30, 40], 25', 'salida_esperada': '0'},
    {'entrada': '[5, 5, 5, 5, 5], 5', 'salida_esperada': '5'},
    {'entrada': '[1, 2, 3, 4], 4', 'salida_esperada': '1'},
    {'entrada': '[9, 9, 9, 9], 7', 'salida_esperada': '0'}
]






ll =[1, 2, 3, 1, 4, 1], 1
# res = ast.literal_eval(ll)
# print(res[0])
# print(type(res[0]))


def contar_ocurrencias(lista,num_obj):
    contador = 0
    for i in lista:
        if i == num_obj:
            contador += 1
    return contador
            




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

verificar_respuestas(contar_ocurrencias,casos_de_prueba)







        