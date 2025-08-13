def extrair_nomes_objetos(lista_objetos):
    nomes = []
    for objeto in lista_objetos:
        if hasattr(objeto, 'nome'):
            nomes.append(objeto.nome)
    
    return nomes

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

if __name__ == "__main__":
    pessoas = [
        Pessoa("João"),
        Pessoa("Maria"),
        Pessoa("Pedro"),
        Pessoa("Ana"),
        Pessoa("Carlos")
    ]
    
    resultado = extrair_nomes_objetos(pessoas)
    print(f"Nomes extraídos dos objetos: {resultado}")