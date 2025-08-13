def encontrar_numeros_impares(lista_numeros):
    numeros_impares = []
    for numero in lista_numeros:
        if numero % 2 != 0:
            numeros_impares.append(numero)
    
    return numeros_impares

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = encontrar_numeros_impares(numeros)
    print(f"Números ímpares da lista: {resultado}")