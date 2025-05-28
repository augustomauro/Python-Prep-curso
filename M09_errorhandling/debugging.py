def multiplica_por_dos(lista):
    lista_multiplicada = [] # Si no esta definida daria error
    for num in lista:
        lista_multiplicada.append(num*2)

    return lista_multiplicada
    
numeros = [1,2,3,4,5]
resultado = multiplica_por_dos(numeros)
print(resultado)