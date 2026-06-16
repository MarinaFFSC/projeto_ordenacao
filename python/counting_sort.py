# arquivo: counting_sort.py

def counting_sort(arr, k):
    """
    Ordena uma lista usando o algoritmo Counting Sort.
    arr: a lista de números a ser ordenada
    k: o maior número possível dentro da lista
    """
    n = len(arr)
    if n == 0:
        return []
        
    # 1. Cria as "caixas" preenchidas com zero
    cnt = [0] * (k + 1)
    
    # 2. Conta quantas vezes cada número aparece
    for v in arr:
        cnt[v] += 1
        
    # 3. Acumula os valores para saber a posição correta de cada número
    for i in range(1, k + 1):
        cnt[i] += cnt[i - 1]
        
    # 4. Cria a lista de saída organizada
    out = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        out[cnt[v] - 1] = v
        cnt[v] -= 1
        
    return out