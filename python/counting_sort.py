def counting_sort(arr, k):
    """
    Ordena uma lista usando o algoritmo Counting Sort.
    arr: a lista de números a ser ordenada
    k: o maior número possível dentro da lista
    """
    n = len(arr)
    if n == 0:
        return []
        
    # cria as caixas com zero
    cnt = [0] * (k + 1)
    
    # conta quantas vezes cada número aparece
    for v in arr:
        cnt[v] += 1
        
    # acumula os valores p/ saber a posição correta de cada numero
    for i in range(1, k + 1):
        cnt[i] += cnt[i - 1]
        
    # cria lista de saída organizada
    out = [0] * n
    for i in range(n - 1, -1, -1):
        v = arr[i]
        out[cnt[v] - 1] = v
        cnt[v] -= 1
        
    return out