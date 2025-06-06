import os
import matplotlib.pyplot as plt

# Lê o arquivo de texto
with open("kmers2_exclusivos_por_familia.txt", "r", encoding="utf-8", errors="replace") as f:
    linhas = f.readlines()

# Organiza os dados
familia_kmers = {}
familia_atual = None

for linha in linhas:
    linha = linha.strip()
    if linha.startswith("Fam"):
        familia_atual = linha.split(":")[1].strip().replace("�", "í")
        familia_kmers[familia_atual] = []
    elif linha.startswith("Exclusivo:") and familia_atual:
        kmer = linha.split(":")[1].strip()
        familia_kmers[familia_atual].append(kmer)

# Criar pasta para os gráficos
os.makedirs("graficos_kmers_exclusivos_por_familia", exist_ok=True)

# Gerar gráfico por família
for familia, kmers in familia_kmers.items():
    plt.figure(figsize=(8, max(2, len(kmers) * 0.4)))
    y_pos = list(range(len(kmers)))
    plt.barh(y_pos, [1]*len(kmers), color="#2063b5")
    plt.yticks(y_pos, kmers)
    plt.xticks([])  # Remove eixo X pois não tem valor quantitativo
    plt.title(f"K-mers exclusivos - {familia}")
    plt.tight_layout()
    # Salva o gráfico
    filename = f"graficos_kmers_exclusivos_por_familia/{familia.replace('/', '_')}_kmers.png"
    plt.savefig(filename, dpi=300)
    plt.close()

print("✅ Gráficos salvos na pasta 'graficos_kmers_exclusivos_por_familia'")
