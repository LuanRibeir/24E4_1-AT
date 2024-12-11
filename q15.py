# Classe que representa um nó na arvore Binaria de Busca
class Node:
    def __init__(self, chave):
        self.chave = chave  # Chave armazenada no nó
        self.esquerda = None  # Referencia para o nó filho a esquerda
        self.direita = None  # Referencia para o nó filho a direita

class BST:
    # Classe para construcao
    def __init__(self):
        self.root = None  
    
    # Metodo publico para inserir uma chave na arvore
    def insert(self, chave):
        if self.root is None:
            # Caso a arvore esteja vazia, cria a raiz
            self.root = Node(chave)
        else:
            # Insere a chave na subarvore apropriada
            self._insert(self.root, chave)

    # Metodo auxiliar para realizar a insercao recursivamente
    def _insert(self, no_atual, chave):
        if chave < no_atual.chave:
            # Se a chave for menor que a do nó atual, vai para a subarvore a esquerda
            if no_atual.esquerda is None:
                # Se nao houver nó a esquerda, insere a chave
                no_atual.esquerda = Node(chave)
            else:
                # Caso contrario, continua recursivamente na subarvre a esquerda
                self._insert(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            # Se a chave for maior que a do no atual, vai para a subarvore a direita
            if no_atual.direita is None:
                # Se nao houver no a direita, insere a chave aqui
                no_atual.direita = Node(chave)
            else:
                # Caso contrario, continua recursivamente na subarvore a direita
                self._insert(no_atual.direita, chave)

    # Metodo para buscar a nota minima na arvore
    def min(self):
        return self._min(self.root)

    # Metodo auxiliar para encontrar a nota minima
    def _min(self, no_atual):
        if no_atual is None:
            return None
        while no_atual.esquerda is not None:
            # A nota minima esta sempre na subarvore aesquerda
            no_atual = no_atual.esquerda
        return no_atual.chave

    # Metodo para buscar a nota maxima na arvore
    def max(self):
        return self._max(self.root)

    # Metodo auxiliar para encontrar a nota maxima
    def _max(self, no_atual):
        if no_atual is None:
            return None
        while no_atual.direita is not None:
            # A nota maxima esta sempre na subarvore a direita
            no_atual = no_atual.direita
        return no_atual.chave


# Uso
if __name__ == "__main__":
    # Lista de notas a serem inseridas
    notas = [85, 70, 95, 60, 75, 90, 100]

    # Inicializa a arvore
    tree = BST()

    # Insere cada nota na arvore
    for nota in notas:
        tree.insert(nota)

    # Encontra e exibe a nota minima
    nota_minima = tree.min()
    print(f"A menor nota na turma é: {nota_minima}")

    # Encontra e exibe a nota maxima
    nota_maxima = tree.max()
    print(f"A maior nota na turma é: {nota_maxima}")
