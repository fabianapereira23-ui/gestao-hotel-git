clientes = []

def registar_cliente(nome_cliente):
    clientes.append(nome_cliente)
    print("Cliente registado!")

def listar_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print(cliente)


def remover_cliente(nome_cliente):
    if nome_cliente in clientes:
        clientes.remove(nome_cliente)
        print("Cliente removido com sucesso.")
    else:
        print("Cliente não encontrado.")