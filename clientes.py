clientes = []

def registar_cliente(nome_cliente):
    clientes.append(nome_cliente)
    print("Cliente registado!")

def listar_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print(cliente)