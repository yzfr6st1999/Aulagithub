def somar_valores_lista(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    
    return soma

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = somar_valores_lista(numeros)
    print(f"A soma de todos os valores da lista é: {resultado}")