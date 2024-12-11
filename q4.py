import random

# Lista ordenada de ISBNs
isbn_list = list(range(1, 100001))  # 100 mil elementos

def busca_linear(lista, isbn):
    iteracoes = 0
    for i, valor in enumerate(lista):
        iteracoes += 1
        if valor == isbn:
            return i, iteracoes
    return "Não encontrado", iteracoes

def busca_binaria(lista, isbn):
    inicio, fim = 0, len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        
        if lista[meio] == isbn:
            return meio, iteracoes
        elif lista[meio] < isbn:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return "Não encontrado", iteracoes

# Testes
for i in range(1,4):
    # ISBN procurado aleatório
    isbn_procurado = random.choice(isbn_list)
    
    print(f"ISBN Procurado: {isbn_procurado}")
    
    # Teste da busca binária
    resultado, iteracoes_binaria = busca_binaria(isbn_list, isbn_procurado)
    print(f"Iterações na busca binária: {iteracoes_binaria}")

    # Teste da busca linear
    _, iteracoes_linear = busca_linear(isbn_list, isbn_procurado)
    print(f"Iterações na busca linear: {iteracoes_linear}\n")
