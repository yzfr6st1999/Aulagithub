def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    
    return contador

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    valor_teste_1 = 2
    valor_teste_2 = 13
    valor_teste_3 = 9
    valor_teste_4 = 100
    
    resultado_1 = contar_ocorrencias(numeros, valor_teste_1)
    resultado_2 = contar_ocorrencias(numeros, valor_teste_2)
    resultado_3 = contar_ocorrencias(numeros, valor_teste_3)
    resultado_4 = contar_ocorrencias(numeros, valor_teste_4)
    
    print(f"O valor {valor_teste_1} aparece {resultado_1} vez(es) na lista")
    print(f"O valor {valor_teste_2} aparece {resultado_2} vez(es) na lista")
    print(f"O valor {valor_teste_3} aparece {resultado_3} vez(es) na lista")
    print(f"O valor {valor_teste_4} aparece {resultado_4} vez(es) na lista")