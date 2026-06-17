#include <iostream>
#include <vector>
#include <chrono>
#include <cstdlib>
#include <cstdio>

//  algoritmo counting sort 
void counting_sort(const int *arr, int *out, int n, int k) {
    // c/ vetor dinamico p/ garantir limpeza automática de memória
    std::vector<int> cnt(k + 1, 0);
    
    for (int i = 0; i < n; i++) 
        cnt[arr[i]]++;
        
    for (int i = 1; i <= k; i++) 
        cnt[i] += cnt[i - 1];
        
    for (int i = n - 1; i >= 0; i--) {
        int v = arr[i];
        out[cnt[v] - 1] = v;
        cnt[v]--;
    }
}

// benchmark c++
void rodar_cenario(FILE *f, int n, const char* nome_cenario, int* dados, int rodadas) {
    std::vector<int> out(n, 0);

    for (int r = 0; r < rodadas; r++) {
        std::vector<int> copia(dados, dados + n);

        auto start = std::chrono::high_resolution_clock::now();

        for (int i = 0; i < 100; i++) {
            counting_sort(copia.data(), out.data(), n, n);
        }

        auto end = std::chrono::high_resolution_clock::now();

        double tempo_ms =
            std::chrono::duration<double, std::milli>(end - start).count() / 100.0;
        printf("VERSAO NOVA\n");
        fprintf(f, "%d,%s,%.8f\n", n, nome_cenario, tempo_ms);
    }
}
int main() {
    int tamanhos[] = {1000, 10000, 100000};
    int rodadas = 30;
    srand(42);

    FILE *f = fopen("tempos_c.txt", "w");
    if (f == NULL) {
        printf("Erro ao criar o arquivo tempos_c.txt\n");
        return 1;
    }
    
    fprintf(f, "tamanho,cenario,tempo_ms\n");
    printf("VERSAO NOVA DO BENCHMARK\n");
    printf("Iniciando Benchmark em C++... Aguarde.\n");

    for(int t = 0; t < 3; t++) {
        int n = tamanhos[t];
        
        std::vector<int> melhor(n);
        std::vector<int> medio(n);
        std::vector<int> pior(n);

        // pra preencher cenario teste
        for(int i = 0; i < n; i++) {
            melhor[i] = i;
            medio[i] = rand() % n;
            pior[i] = n - i;
        }

        rodar_cenario(f, n, "Melhor", melhor.data(), rodadas);
        rodar_cenario(f, n, "Medio", medio.data(), rodadas);
        rodar_cenario(f, n, "Pior", pior.data(), rodadas);
    }

    fclose(f);
    printf("Benchmark em C++ concluido! Arquivo 'tempos_c.txt' gerado com sucesso.\n");
    return 0;
}