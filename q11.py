class FilaDeAtendimento:
    def __init__(self):
        self.fila = []  # lista para armazenar os chamados

    def adicionar(self, chamado):
        self.fila.append(chamado)
        print(f"Chamado '{chamado}' adicionado na fila.")

    def atender(self):
        if self.fila:
            chamado_atendido = self.fila.pop(0)  # Remove o primeiro chamado da fila
            print(f"Chamado '{chamado_atendido}' atendido e removido da fila.")
        else:
            print("Não há chamados na fila.")

    def visualizar_fila(self):
        if self.fila:
            print("Chamados na fila:", self.fila)
        else:
            print("A fila está vazia.")

# Exemplo
fila_atendimento = FilaDeAtendimento()

fila_atendimento.adicionar("Chamado 1")
fila_atendimento.adicionar("Chamado 2")
fila_atendimento.adicionar("Chamado 3")
fila_atendimento.adicionar("Chamado 4")

fila_atendimento.visualizar_fila()

fila_atendimento.atender()
fila_atendimento.atender()

fila_atendimento.visualizar_fila()

fila_atendimento.atender()
fila_atendimento.atender()

fila_atendimento.visualizar_fila()
