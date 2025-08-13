def inverter_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    
    return lista_invertida

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = inverter_lista(numeros)
    print(f"Lista original: {numeros}")
    print(f"Lista invertida: {resultado}")