
#kmers que mais se repetem entre todas as famílias 
# Este script analisa os arquivos *_top20_kmers.csv e gera um CSV com os k-mers mais frequentes
# e as famílias em que aparecem, ordenados pela frequência de ocorrência.
import pandas as pd
import glob
from collections import defaultdict

# Encontra todos os arquivos *_top20_kmers.csv
arquivos = glob.glob("*_top20_kmers.csv")

# Dicionário para armazenar os k-mers e as famílias em que aparecem
kmers_por_familia = defaultdict(set)  # kmer: set de famílias

for arquivo in arquivos:
    nome_familia = arquivo.split("_top20_kmers.csv")[0]  # Extrai o nome da família do nome do arquivo
    df = pd.read_csv(arquivo)
    kmers = df['kmer'].astype(str).str.upper().tolist()  # Garante string maiúscula
    for kmer in kmers:
        kmers_por_familia[kmer].add(nome_familia)

# Converte para DataFrame
dados = []
for kmer, familias in kmers_por_familia.items():
    dados.append({
        "kmer": kmer,
        "ocorrencias": len(familias),
        "familias": ";".join(sorted(familias))  # separadas por ponto e vírgula
    })

df_final = pd.DataFrame(dados)
df_final = df_final.sort_values(by="ocorrencias", ascending=False)

# Mostra os top 10
print(df_final.head(10))

# Salva em CSV
df_final.to_csv("kmer2_ocorrencias_com_nome_familias.csv", index=False)

