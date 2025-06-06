# #dentre os 20 kmers que mais se repetem, existe algum que é exclusivo de cada familia em expecifico
# #kmers que estão no top 20 de uma família e não aparecem nos top 20 de nenhuma outra


import pandas as pd
import glob
from Bio import SeqIO

# === ETAPA 1: Lê os arquivos *_top20_kmers.csv e agrupa os k-mers por família ===
arquivos = glob.glob("*_top20_kmers.csv")
familia_kmers = {}

for arquivo in arquivos:
    familia = arquivo.replace("_top20_kmers.csv", "")
    df = pd.read_csv(arquivo)
    kmers = set(df['kmer'].astype(str).str.upper())
    familia_kmers[familia] = kmers

# === ETAPA 2: Descobre k-mers exclusivos (que não aparecem nas outras famílias) ===
exclusivos_por_familia = {}

for familia, kmers in familia_kmers.items():
    outros_kmers = set().union(*[v for k, v in familia_kmers.items() if k != familia])
    exclusivos = kmers - outros_kmers
    exclusivos_por_familia[familia] = exclusivos

# === ETAPA 3: Salva os k-mers exclusivos em arquivo .txt (resumo) ===
with open("kmers2_exclusivos_por_familia.txt", "w") as f:
    for familia, exclusivos in exclusivos_por_familia.items():
        f.write(f"Família: {familia}\n")
        if exclusivos:
            for kmer in exclusivos:
                f.write(f"  Exclusivo: {kmer}\n")
        else:
            f.write("  Nenhum k-mer exclusivo.\n")
        f.write("\n")

# === ETAPA 4: Conta quantas sequências da própria família contêm o k-mer exclusivo ===
todos_resultados = []

for familia, exclusivos in exclusivos_por_familia.items():
    arquivo_fasta = f"{familia}.fasta"
    
    try:
        sequencias = [str(record.seq).upper() for record in SeqIO.parse(arquivo_fasta, "fasta")]
        print(f"{familia}: {len(sequencias)} sequências no total")
    except FileNotFoundError:
        print(f"Arquivo .fasta não encontrado para {familia}")
        continue

    resultados = []
    for kmer in exclusivos:
        ocorrencias = sum(1 for seq in sequencias if kmer in seq)
        resultados.append({
            "familia": familia,
            "kmer_exclusivo": kmer,
            "n_sequencias_com_esse_kmer": ocorrencias
        })

    df_resultado = pd.DataFrame(resultados)
    df_resultado.to_csv(f"{familia}_kmers_exclusivos_e_ocorrencias.csv", index=False)
    todos_resultados.append(df_resultado)
    print(f"Salvo: {familia}_kmers_exclusivos_e_ocorrencias.csv")

# === ETAPA 5: Consolida todos os resultados em um único CSV final ===
if todos_resultados:
    df_final = pd.concat(todos_resultados, ignore_index=True)
    df_final.to_csv("todos_kmers_exclusivos_com_ocorrencias.csv", index=False)
    print("Arquivo único salvo: todos_kmers_exclusivos_com_ocorrencias.csv")
