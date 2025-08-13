def remover_duplicatas(lista):
    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    
    return lista_unica

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = remover_duplicatas(numeros)
    print(f"Lista original: {numeros}")
    print(f"Lista sem duplicatas: {resultado}")
    print(f"Tamanho da lista original: {len(numeros)}")
    print(f"Tamanho da lista sem duplicatas: {len(resultado)}")