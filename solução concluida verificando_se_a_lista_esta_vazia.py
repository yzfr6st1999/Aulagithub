def verificar_lista_vazia(lista):
    return len(lista) == 0

if __name__ == "__main__":
    lista_vazia = []
    lista_com_elementos = [1, 2, 3]
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    
    resultado_1 = verificar_lista_vazia(lista_vazia)
    resultado_2 = verificar_lista_vazia(lista_com_elementos)
    resultado_3 = verificar_lista_vazia(numeros)
    
    print(f"Lista vazia está vazia: {resultado_1}")
    print(f"Lista com elementos [1, 2, 3] está vazia: {resultado_2}")
    print(f"Lista fornecida está vazia: {resultado_3}")