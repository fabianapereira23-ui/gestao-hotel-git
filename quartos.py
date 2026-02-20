quartos = {}
def adicionar_quarto(numero):
    quartos[numero] = "disponivel"
    print("Quarto adicionado como disponível.")
    
def listar_quartos():
    for numero in quartos:
        print(numero)