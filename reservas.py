reservas = []

def criar_reserva(nome_cliente):
    reservas.append(nome_cliente)
    print("Reserva criada.")

def listar_reservas():
    for reserva in reservas:
        print(reserva)