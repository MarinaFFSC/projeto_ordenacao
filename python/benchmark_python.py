# arquivo: benchmark_python.py
import time
import random
from counting_sort import counting_sort

# Configurações seguras para 4GB de RAM
tamanhos = [1000, 10000, 100000]
rodadas = 30
random.seed(42)

print("Iniciando Benchmark em Python... Aguarde.")

with open("tempos_python.txt", "w") as f:
    f.write("tamanho,cenario,tempo_ms\n")
    
    for n in tamanhos:
        k = n  # O maior número será igual ao tamanho da lista
        
        # Cenários solicitados pelo professor
        cenarios = {
            "Melhor": list(range(n)),
            "Medio": [random.randint(0, k) for _ in range(n)],
            "Pior": list(range(n, -1, -1))
        }
        
        for nome, dados_originais in cenarios.items():
            for _ in range(rodadas):
                # Fazemos uma cópia para não estragar o cenário nas próximas rodadas
                lista_copia = dados_originais.copy() 
                
                # Medição com alta precisão
                t_inicio = time.perf_counter()
                for _ in range(100):
                    counting_sort(lista_copia, k)
                t_fim = time.perf_counter()
                
                tempo_ms = ((t_fim - t_inicio) * 1000) / 100
                f.write(f"{n},{nome},{tempo_ms:.8f}\n")

print("Benchmark em Python concluído! Arquivo 'tempos_python.txt' gerado.")