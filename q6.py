import time
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Testa o algoritimo nois dois tamanhos de lista
for tamanho in [1000, 10000]:
    lista = [random.randint(1, 10000) for _ in range(tamanho)]
    
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    
    print(f"Bubble Sort com {tamanho} elementos: {fim - inicio:.4f}s")
