# Projeto Teoria da Complexidade e Análise do Algoritmo Counting Sort

## Descrição

Este projeto foi desenvolvido para a disciplina de **Teoria da Computação**, com o objetivo de realizar uma análise experimental do algoritmo **Counting Sort**, comparando seu desempenho nas linguagens **Python** e **C++**.

A avaliação foi conduzida por meio de experimentos controlados, considerando diferentes tamanhos de entrada, múltiplas execuções e cenários de teste distintos. Os resultados obtidos foram comparados com a complexidade teórica esperada do algoritmo.

---

## Objetivos

* Implementar o algoritmo Counting Sort em Python e C++.
* Avaliar o desempenho em diferentes tamanhos de entrada.
* Comparar os tempos médios de execução entre as linguagens.
* Verificar a aderência dos resultados experimentais à complexidade teórica do algoritmo.
* Aplicar análise estatística por meio de média e desvio padrão.
* Produzir gráficos para visualização e interpretação dos resultados.

---

## Algoritmo Avaliado

O Counting Sort é um algoritmo de ordenação não comparativo que utiliza a contagem da frequência dos elementos para realizar a ordenação.

### Complexidade Teórica

| Caso        | Complexidade |
| ----------- | ------------ |
| Melhor Caso | O(n + k)     |
| Caso Médio  | O(n + k)     |
| Pior Caso   | O(n + k)     |

Nos experimentos realizados, foi adotado:

```text
k = n
```

Portanto:

```text
O(n + k) = O(2n) = O(n)
```

---

## Configuração dos Testes

### Tamanhos de Entrada

| Tamanho |
| ------- |
| 1.000   |
| 10.000  |
| 100.000 |

### Cenários Avaliados

#### Melhor Caso

Entrada já ordenada.

Exemplo:

```text
[1, 2, 3, 4, 5, ...]
```

#### Caso Médio

Entrada com distribuição aleatória.

#### Pior Caso

Entrada em ordem inversa.

Exemplo:

```text
[100000, 99999, 99998, ...]
```

### Protocolo Experimental

* 30 execuções para cada cenário.
* 30 execuções para cada tamanho de entrada.
* Execução nas linguagens Python e C++.
* Cálculo de média e desvio padrão.
* Medição utilizando temporizadores de alta precisão.

---

## Gráficos Produzidos

O projeto gera automaticamente os seguintes gráficos:

1. Melhor Caso
2. Caso Médio
3. Pior Caso
4. Comparação Geral Python × C++
5. Speedup (Python/C++)
6. Desvio Padrão das Execuções
7. Aderência à Complexidade Teórica
8. Boxplot das Execuções em Python
9. Boxplot das Execuções em C++

---

## Ferramentas Utilizadas

### Linguagens

* Python 3
* C++17

### Bibliotecas Python

* pandas
* numpy
* matplotlib

### Ambiente

* Visual Studio Code
* Git
* GitHub

---
Curso de Ciência da Computação

