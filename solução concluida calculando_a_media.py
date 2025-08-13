def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    
    soma = 0
    for numero in lista_numeros:
        soma += numero
    
    media = soma / len(lista_numeros)
    return media

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = calcular_media(numeros)
    print(f"A média aritmética dos valores da lista é: {resultado:.2f}")
    print(f"Soma total: {sum(numeros)}")
    print(f"Quantidade de elementos: {len(numeros)}")