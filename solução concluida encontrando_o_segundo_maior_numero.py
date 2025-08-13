def encontrar_segundo_maior_numero(lista_numeros):
    if len(lista_numeros) < 2:
        return None
    
    numeros_unicos = list(set(lista_numeros))
    numeros_unicos.sort(reverse=True)
    
    if len(numeros_unicos) >= 2:
        return numeros_unicos[1]
    else:
        return None

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = encontrar_segundo_maior_numero(numeros)
    print(f"O segundo maior número da lista é: {resultado}")