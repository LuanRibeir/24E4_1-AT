class HashTable:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade  # Tamanho da tabela
        self.tabela = [[] for _ in range(capacidade)]  # Lista para encadeamento
        self.size = 0  # Contador de elementos

    def hash(self, chave):
        # Função que retorna um indice
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        indice = self.hash(chave)  
        for par in self.tabela[indice]: 
            if par[0] == chave:
                par[1] = valor
                return
    
        self.tabela[indice].append([chave, valor])
        self.size += 1  

    def buscar(self, chave):
        indice = self.hash(chave)  
        for par in self.tabela[indice]: 
            if par[0] == chave:
                return par[1]  
        return None 


def verifica_duplicatas(lista):
    # Instancia uma tabela hash com tamanho da lista
    tabela_hash = HashTable(len(lista))
    
    for elemento in lista:
        # Verifica se o elemento ja esta na tabela hash
        if tabela_hash.buscar(elemento) is not None:
            return True  # Retorna True se encontrar duplicata
        
        # Caso contrario, insere o elemento na tabela
        tabela_hash.inserir(elemento, True)
    
    return False  # Retorna False se não houver duplicatas

# Testes
lista_com_dup = [1, 1, 2, 3, 4, 5]
print(f"{lista_com_dup} {verifica_duplicatas(lista_com_dup)}")  # True

lista_sem_dup = [1, 2, 3, 4, 5]
print(f"{lista_sem_dup} {verifica_duplicatas(lista_sem_dup)}")  # False
