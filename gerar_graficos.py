import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dados
df_py = pd.read_csv("tempos_python.txt")
df_c = pd.read_csv("C++/tempos_c.txt")

# evitar problemas c/ log(0)
df_py["tempo_ms"] = df_py["tempo_ms"].clip(lower=0.000001)
df_c["tempo_ms"] = df_c["tempo_ms"].clip(lower=0.000001)

# médias e desvios

py_stats = (
    df_py.groupby(["tamanho", "cenario"])["tempo_ms"]
    .agg(["mean", "std"])
    .reset_index()
)

c_stats = (
    df_c.groupby(["tamanho", "cenario"])["tempo_ms"]
    .agg(["mean", "std"])
    .reset_index()
)

cenarios = ["Melhor", "Medio", "Pior"]

# gráficos 1,2,3
# cenários

for cenario in cenarios:

    plt.figure(figsize=(8,5))

    py = py_stats[py_stats["cenario"] == cenario]
    c = c_stats[c_stats["cenario"] == cenario]

    plt.plot(
        py["tamanho"],
        py["mean"],
        marker="o",
        label="Python"
    )

    plt.plot(
        c["tamanho"],
        c["mean"],
        marker="s",
        label="C++"
    )

    base = c["mean"].iloc[0]
    n0 = c["tamanho"].iloc[0]

    teorica = [base * (n/n0) for n in c["tamanho"]]

    plt.plot(
        c["tamanho"],
        teorica,
        "--",
        label="O(n)"
    )

    plt.xscale("log")
    plt.yscale("log")

    plt.title(f"Counting Sort - {cenario}")
    plt.xlabel("Tamanho da Entrada")
    plt.ylabel("Tempo Médio (ms)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        f"grafico_{cenario.lower()}.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

# grafico 4
# comparação geral

py_geral = df_py.groupby("tamanho")["tempo_ms"].mean()
c_geral = df_c.groupby("tamanho")["tempo_ms"].mean()

plt.figure(figsize=(8,5))

plt.plot(
    py_geral.index,
    py_geral.values,
    marker="o",
    label="Python"
)

plt.plot(
    c_geral.index,
    c_geral.values,
    marker="s",
    label="C++"
)

plt.xscale("log")
plt.yscale("log")

plt.title("Comparação Geral")
plt.xlabel("Tamanho")
plt.ylabel("Tempo Médio (ms)")
plt.legend()
plt.grid(True)

plt.savefig(
    "grafico_comparacao_geral.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# gráfico 5
# speedup

speedup = py_geral / c_geral

plt.figure(figsize=(8,5))

plt.plot(
    speedup.index,
    speedup.values,
    marker="o"
)

plt.xscale("log")

plt.title("Speedup (Python/C++)")
plt.xlabel("Tamanho")
plt.ylabel("Speedup")
plt.grid(True)

plt.savefig(
    "grafico_speedup.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# gráfico 6
# desvio padrão

py_std = df_py.groupby("tamanho")["tempo_ms"].std()
c_std = df_c.groupby("tamanho")["tempo_ms"].std()

x = np.arange(len(py_std.index))
largura = 0.35

plt.figure(figsize=(9,5))

plt.bar(
    x - largura/2,
    py_std.values,
    largura,
    label="Python"
)

plt.bar(
    x + largura/2,
    c_std.values,
    largura,
    label="C++"
)

plt.xticks(x, py_std.index)

# melhoria
plt.yscale("log")

plt.title("Desvio Padrão das Execuções")
plt.xlabel("Tamanho")
plt.ylabel("Desvio Padrão (Escala Log)")
plt.legend()
plt.grid(True, axis="y", alpha=0.3)

plt.savefig(
    "grafico_desvio_padrao.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# gráfico 7
# aderência teória


plt.figure(figsize=(8,5))

# tempos médios medidos em C++
tempos_reais = c_geral.values
n = np.array(c_geral.index)

# curva teórica O(n) ajustada ao primeiro ponto real
base_tempo = tempos_reais[0]
base_n = n[0]

curva_teorica = [
    base_tempo * (valor_n / base_n)
    for valor_n in n
]

plt.plot(
    n,
    tempos_reais,
    marker="o",
    linewidth=2,
    label="Tempo Medido (C++)"
)

plt.plot(
    n,
    curva_teorica,
    "--",
    linewidth=2,
    label="Curva Teórica O(n)"
)

plt.xscale("log")
plt.yscale("log")

plt.title("Aderência à Complexidade Teórica")
plt.xlabel("Tamanho da Entrada (N)")
plt.ylabel("Tempo Médio de Execução (ms)")
plt.legend()
plt.grid(True)

plt.savefig(
    "grafico_aderencia_teorica.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# gráfico 8.1
# boxplot python


dados_py = []
labels_py = []

for tamanho in sorted(df_py["tamanho"].unique()):

    dados_py.append(
        df_py[df_py["tamanho"] == tamanho]["tempo_ms"]
    )

    labels_py.append(str(tamanho))

plt.figure(figsize=(8,5))

plt.boxplot(
    dados_py,
    tick_labels=labels_py
)

plt.title("Distribuição dos Tempos - Python")
plt.xlabel("Tamanho da Entrada")
plt.ylabel("Tempo (ms)")

plt.savefig(
    "grafico_boxplot_python.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# gráfico 8.2
# boxplot c++


dados_c = []
labels_c = []

for tamanho in sorted(df_c["tamanho"].unique()):

    dados_c.append(
        df_c[df_c["tamanho"] == tamanho]["tempo_ms"]
    )

    labels_c.append(str(tamanho))

plt.figure(figsize=(8,5))

plt.boxplot(
    dados_c,
    tick_labels=labels_c
)

plt.title("Distribuição dos Tempos - C++")
plt.xlabel("Tamanho da Entrada")
plt.ylabel("Tempo (ms)")

plt.savefig(
    "grafico_boxplot_cpp.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()