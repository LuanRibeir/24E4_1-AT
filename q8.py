def selection_sort(jogadores): 
    n = len(jogadores) # Salva o tamanho da lista na variavel
    
    # Loop externo percorre cada posição da lista
    for i in range(n):
        # Assume que o menor elemento esta na posiçao i
        min_idx = i
        
        # Loop interno busca o menor elemento na sublista que começa na posição i+1
        for j in range(i + 1, n):
            # Compara as pontuações para encontrar o menor valor
            # Vai resultar em uma ordem decrescente
            if jogadores[j]['pontuacao'] > jogadores[min_idx]['pontuacao']:
                min_idx = j  # Atualiza o indice do menor elemento
        
        # Troca o menor elemento encontrado com o elemento da posição i
        jogadores[i], jogadores[min_idx] = jogadores[min_idx], jogadores[i]

    # Retorna a lista de jogadores ordenada
    return jogadores

# Teste
jogadores = [
    {"nome": "Rere", "pontuacao": 1111},
    {"nome": "Tete", "pontuacao": 2222},
    {"nome": "Yeye", "pontuacao": 34},
    {"nome": "Ueue", "pontuacao": 4444},
    {"nome": "Pepe", "pontuacao": 90},
    {"nome": "Meme", "pontuacao": 1},
]

selection_sort(jogadores)

# Imprimindo os jogadores ordenados
for jogador in jogadores:
    print(f"{jogador['nome']} - {jogador['pontuacao']} pontos")