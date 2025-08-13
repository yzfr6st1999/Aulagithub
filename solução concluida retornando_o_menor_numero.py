def retornar_menor_numero(lista_numeros):
    if not lista_numeros:
        return None
    
    menor = lista_numeros[0]
    for numero in lista_numeros:
        if numero < menor:
            menor = numero
    
    return menor

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = retornar_menor_numero(numeros)
    print(f"O menor número da lista é: {resultado}")