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

    # Metodo para remover uma chave na arvore
    def remove(self, chave):
        self.root = self._remove(self.root, chave)

    # Metodo auxiliar para remover recursivamente
    def _remove(self, node, chave):
        if node is None:
            return node

        if chave < node.chave:
            # Se a chave for menor, remove na subarvore da esquerda
            node.esquerda = self._remove(node.esquerda, chave)
        elif chave > node.chave:
            # Se a chave for maior, remove na subarvore da direita
            node.direita = self._remove(node.direita, chave)
        else:
            # Caso a chave seja encontrada
            # Nó sem filhos
            if node.esquerda is None and node.direita is None:
                return None
            # Nó com um filho
            elif node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            # Nó com dois filhos
            else:
                node.chave = self._valor_min(node.direita)
                node.direita = self._remove(node.direita, node.chave)

        return node

    # Metodo para encontrar o valor minimo na subarvore
    def _valor_min(self, node):
        current_node = node
        while current_node.esquerda is not None:
            current_node = current_node.esquerda
        return current_node.chave

    # Metodo para exibir em ordem crescente
    def em_ordem(self):
        self._em_ordem(self.root)
        print()

    # Metodo auxiliar para exibir em ordem crescente
    def _em_ordem(self, node):
        if node:
            self._em_ordem(node.esquerda)  # Vai a subarvore da esquerda
            print(node.chave, end=' ')  # Exibe o nó atual
            self._em_ordem(node.direita)  # Vai a subarvore da direita


# Uso
if __name__ == "__main__":
    produtos = [45, 25, 65, 20, 30, 60, 70]
    tree = BST()

    for produto in produtos:
        tree.insert(produto)

    print("Árvore inicial:")
    tree.em_ordem()

    tree.remove(20)
    print("Árvore após remover o código 20 (nó folha):")
    tree.em_ordem()

    tree.remove(25)
    print("Árvore após remover o código 25 (nó com um filho):")
    tree.em_ordem()

    tree.remove(45)
    print("Árvore após remover o código 45 (nó com dois filhos):")
    tree.em_ordem()
