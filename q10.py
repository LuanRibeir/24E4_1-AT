class Navegador:
    def __init__(self):
        self.pilha_voltar = []  # Pilha para paginas anteriores
        self.pilha_avancar = []  # Pilha para paginas para avançar
        self.pagina_atual = None  # Pagina atual

    def visitar(self, url):
        if self.pagina_atual:
            self.pilha_voltar.append(self.pagina_atual)  # Adiciona a pagina atual a pilha de pagians anteriores
        self.pagina_atual = url
        self.pilha_avancar.clear()  # Limpa a pilha de avanço quando uma nova pagina é visitaaa

    def voltar(self):
        if self.pilha_voltar:
            self.pilha_avancar.append(self.pagina_atual)  # Adiciona a pagina atual a pilha de avanço
            self.pagina_atual = self.pilha_voltar.pop()  # Retorna para a ultima pagina visitada
        else:
            print("Não há páginas anteriores.")

    def avancar(self):
        if self.pilha_avancar:
            self.pilha_voltar.append(self.pagina_atual)  # Adiciona a pagina atual a pilha de pagina anteriores
            self.pagina_atual = self.pilha_avancar.pop()  # Retorna para a ultima pagina avançada
        else:
            print("Não há páginas para avançar.")

    def get_pagina_atual(self):
        return self.pagina_atual

# Exemplos
nav = Navegador()

nav.visitar("Página 1")
print(f"Visitar\tPágina atual: {nav.get_pagina_atual()}") 

nav.visitar("Página 2")
print(f"Visitar\tPágina atual: {nav.get_pagina_atual()}")  

nav.visitar("Página 3")
print(f"Visitar\tPágina atual: {nav.get_pagina_atual()}")  

nav.voltar()
print(f"Voltar\tPágina atual: {nav.get_pagina_atual()}")  

nav.voltar()
print(f"Voltar\tPágina atual: {nav.get_pagina_atual()}")  

nav.avancar()
print(f"Avançar\tPágina atual: {nav.get_pagina_atual()}")  

nav.avancar()
print(f"Avançar\tPágina atual: {nav.get_pagina_atual()}") 

nav.voltar()
nav.voltar()
nav.voltar()  # sem paginas anteriores
