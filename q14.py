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

    # Metodo para procurar uma chave na arvore
    def procurar(self, chave):
        return self._procurar(self.root, chave)

    # Metodo auxiliar para realizar a busca recursivamente
    def _procurar(self, no_atual, chave):
        if no_atual is None:
            # Se o nó atual for None, a chave nao esta na arvore
            return False
        if no_atual.chave == chave:
            # Caso a chave seja encontrada no nó atual, retorna True
            return True
        elif chave < no_atual.chave:
            # Se a chave for menor, busca na subarvore a esquerda
            return self._procurar(no_atual.esquerda, chave)
        else:
            # Se a chave for maior, busca na subarvore a direita
            return self._procurar(no_atual.direita, chave)


# Uso
if __name__ == "__main__":
    # Lista de precos a serem inseridos
    precos = [100, 50, 150, 30, 70, 130, 170]

    # Inicializa a arvore
    tree = BST()

    # Insere cada preco na arvore
    for preco in precos:
        tree.insert(preco)

    # Verifica se o preco 70 esta disponivel
    preco = 70
    if tree.procurar(preco):
        print(f"Preco {preco} está disponível.")
    else:
        print(f"Preco {preco} não está disponível.")
