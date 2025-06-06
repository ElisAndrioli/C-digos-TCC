#dentre os 20 kmers que mais se repetem, existe algum que é exclusivo de cada familia em expecifico
#kmers que estão no top 20 de uma família e não aparecem nos top 20 de nenhuma outra

import pandas as pd
import glob

# Encontra todos os arquivos *_top20_kmers.csv
arquivos = glob.glob("*_top20_kmers.csv")

# Dicionário: {familia: set(kmers)}
familia_kmers = {}

for arquivo in arquivos:
    familia = arquivo.split("_top20_kmers.csv")[0]  # extrai nome da família
    df = pd.read_csv(arquivo)
    kmers = set(df['kmer'].astype(str).str.upper())
    familia_kmers[familia] = kmers

# Encontra k-mers exclusivos
exclusivos_por_familia = {}

for familia, kmers in familia_kmers.items():
    outros_kmers = set().union(*[v for k, v in familia_kmers.items() if k != familia])
    exclusivos = kmers - outros_kmers
    exclusivos_por_familia[familia] = exclusivos

# Exibe os resultados
for familia, exclusivos in exclusivos_por_familia.items():
    print(f"\nFamília: {familia}")
    if exclusivos:
        for kmer in exclusivos:
            print(f"  Exclusivo: {kmer}")
    else:
        print("  Nenhum k-mer exclusivo.")

# Salva em um arquivo .txt
with open("kmers2_exclusivos_por_familia.txt", "w") as f:
    for familia, exclusivos in exclusivos_por_familia.items():
        f.write(f"Família: {familia}\n")
        if exclusivos:
            for kmer in exclusivos:
                f.write(f"  Exclusivo: {kmer}\n")
        else:
            f.write("  Nenhum k-mer exclusivo.\n")
        f.write("\n")
