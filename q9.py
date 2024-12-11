import random
import time

class HashTable:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade  # Tamanho da tabela
        self.tabela = [[] for _ in range(capacidade)]  # Lista para encadeamento
        self.size = 0  # Contador de elementos

    def hash(self, chave):
        # Função que retorna um indice
        return hash(chave) % self.capacidade

    def inserir(self, nome, perfil):
        indice = self.hash(nome)  # Calcula o indice na tabela hash
        
        # Verifica se o nome de usuario ja existe no indice
        for item in self.tabela[indice]:
            if item[0] == nome:
                item[1] = perfil  # Atualiza o perfil se ja existir
                return
        
        # Adiciona um novo par no indice
        self.tabela[indice].append((nome, perfil))
        self.size += 1  

    def buscar(self, nome):
        indice = self.hash(nome)  # Calcula o indice na tabela hash
        # percorre a lista encadeada no indice indicado
        for par in self.tabela[indice]: 
            if par[0] == nome:
                return par[1]  # Retorna o perfil encontrado
        return None  # Retorna None se não for encontrado


def busca_linear(lista, nome):
    for perfil in lista:
        if perfil["nome"] == nome:
            return perfil
    return None

# Medir tempo para busca na tabela hash fazendo 100 repetições para média
def medir_tempo(buscar, *args, repeticoes=100):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.time()
        retorno_busca = buscar(*args)
        fim = time.time()
        tempos.append(fim - inicio)
    tempo_medio = sum(tempos) / len(tempos)
    return retorno_busca, tempo_medio


random_usuarios = [f"usuario{i}" for i in range(1, 100001)]
random_perfis = [{"nome": f"usuario{i}", 
                  "idade": random.randint(16, 99), 
                  "cidade": f"cidade {random.randint(1, 50)}"} for i in range(1, 100001)]

# Criar a tabela hash
tabela_hash = HashTable(capacidade=100000)
for i in range(len(random_usuarios)):
    tabela_hash.inserir(random_usuarios[i], random_perfis[i])

# Criar a lista de perfis
lista_perfis = []
for i in range(len(random_usuarios)):
    lista_perfis.append({"nome": random_usuarios[i], "perfil": random_perfis[i]})

usuario_procurado = random.choice(random_usuarios)

# Medir tempo para busca na tabela hash
retorno_hash, tempo_hash_medio = medir_tempo(tabela_hash.buscar, usuario_procurado)
print(retorno_hash)
print(f"Tempo médio para busca na tabela hash: {tempo_hash_medio:.10f}s.\n")

# Medir tempo para busca linear
retorno_linear, tempo_linear_medio = medir_tempo(busca_linear, lista_perfis, usuario_procurado)
print(retorno_linear['perfil'])
print(f"Tempo médio para busca linear: {tempo_linear_medio:.10f}s.\n")

