import matplotlib.pyplot as plt
import pandas as pd
import os

# Corrigir acentuação e ler arquivo
with open("kmers2_exclusivos_por_familia.txt", "r", encoding="utf-8", errors="replace") as f:
    linhas = f.readlines()

dados = {}
familia_atual = None

for linha in linhas:
    linha = linha.strip()
    if linha.startswith("Fam"):
        familia_atual = linha.split(":")[1].strip().replace("�", "í")  # Corrige erro de codificação
        dados[familia_atual] = 0
    elif linha.startswith("Exclusivo:") and familia_atual:
        dados[familia_atual] += 1

# Criar DataFrame ordenado
df = pd.DataFrame(list(dados.items()), columns=["Família", "Nº de k-mers exclusivos"])
df = df.sort_values(by="Nº de k-mers exclusivos", ascending=True)

# Salvar como CSV
df.to_csv("tabela_kmers_exclusivos_por_familia.csv", index=False)

# Criar gráfico
plt.figure(figsize=(10, 7))
bars = plt.barh(df["Família"], df["Nº de k-mers exclusivos"], color="#2063b5")

# Adicionar número no final de cada barra
for bar in bars:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center')

plt.xlabel("Número de k-mers exclusivos")
plt.title("Distribuição de k-mers exclusivos por família")
plt.tight_layout()

# Salvar figura
plt.savefig("grafico_kmers_exclusivos_por_familia.png", dpi=300)
plt.show()
