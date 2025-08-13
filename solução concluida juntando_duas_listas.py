def juntar_duas_listas(lista1, lista2):
    lista_concatenada = []
    
    for item in lista1:
        lista_concatenada.append(item)
    
    for item in lista2:
        lista_concatenada.append(item)
    
    return lista_concatenada

if __name__ == "__main__":
    lista_a = [1, 2, 3, 4]
    lista_b = [5, 6, 7, 8, 9]
    numeros_parte1 = [987654321, 2, 7654321, 56, 1234567]
    numeros_parte2 = [1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    
    resultado_1 = juntar_duas_listas(lista_a, lista_b)
    resultado_2 = juntar_duas_listas(numeros_parte1, numeros_parte2)
    
    print(f"Lista A: {lista_a}")
    print(f"Lista B: {lista_b}")
    print(f"Listas A + B: {resultado_1}")
    print()
    print(f"Números parte 1: {numeros_parte1}")
    print(f"Números parte 2: {numeros_parte2}")
    print(f"Lista completa reunida: {resultado_2}")