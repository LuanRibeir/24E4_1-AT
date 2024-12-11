# Soluciona o problema da mochila, retornando o melhor valor possível
def knapsack(pesos, valores, capacidade):
    n = len(valores)  # Número de itens
    # tabela dp[i][w] representa o valor máximo para os primeiros i itens e capacidade w
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    # Construção da tabela
    for i in range(1, n + 1):  # Itera sobre os itens
        for w in range(1, capacidade + 1): 
            # Se o peso do item atual for menor ou igual a capacidade w,
            # o item pode ser incluido na mochila.
            if pesos[i - 1] <= w: 
                # Escolhe a melhor opção entre duas possibilidades para o item atual i e a capacidade atual da mochila w
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidade] 

# Exemplo
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidade = 50

resultado = knapsack(pesos, valores, capacidade)
print(f"Valor máximo que pode ser carregado: {resultado}")
