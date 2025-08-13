def buscar_numero(numero, lista):
    for item in lista:
        if item == numero:
            return True
    return False

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    numero_busca_1 = 42
    numero_busca_2 = 100
    
    resultado_1 = buscar_numero(numero_busca_1, numeros)
    resultado_2 = buscar_numero(numero_busca_2, numeros)
    
    print(f"O número {numero_busca_1} está na lista: {resultado_1}")
    print(f"O número {numero_busca_2} está na lista: {resultado_2}")