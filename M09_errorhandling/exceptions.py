def divide_elementos_de_lista(lista, divisor):
    '''
    Cada elemento de una lista es dividida por un divisor definido.
    En caso de error de tipo ZeroDivisionError que
    significa error al dividir en cero
    la función devuelve la lista inicial
    '''
    try:
        return [i / divisor for i in lista]
    
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))
# division by zero
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
divisor = 3
print(divide_elementos_de_lista(lista, divisor))
[0.0, 0.3333333333333, 0.6666666666666, 1.0, 1.3333333333333, 1.6666666666667, 2.0, 2.3333333333335, 2.6666666666665, 3.0]

# -------------------------------------

def dividir(num1,num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print('No se puede dividir por cero!')
        return None
    
print(dividir(4,2))
print(dividir(1,0))

# -------------------------------------

def abrir_archivo():
    try:
        with open('archivo.txt', 'r') as f:
            contenido = f.read()
    except FileNotFoundError:
        print('El archivo no existe!')
        
print(abrir_archivo())

# -------------------------------------

def busca_pais(paises, pais):
    '''
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    '''

    try:
        return paises[pais]
    except KeyError:
        return None
    
print(busca_pais({'Argentina':1,'Brasil':2}, 'Uruguay'))