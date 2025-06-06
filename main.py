#kmers mais comuns em cada uma das familias

from kmer import kmer_profile
from collections import Counter
import pandas as pd

# Parâmetros
fasta_file = "Asfaviridae.fasta"
k = 6

# Gera os perfis k-mer (dicionário: {nome_da_sequência: {kmer: contagem}})
profiles = kmer_profile(fasta_file, k)

# Contador global de k-mers
global_counter = Counter()

# Soma todos os k-mers de todas as sequências
for profile in profiles.values():
    global_counter.update(profile)

# Pega os 20 k-mers mais frequentes
top20 = global_counter.most_common(20)

# Exibe
print("Top 20 k-mers mais comuns:")
for kmer, freq in top20:
    print(f"{kmer}\t{freq}")

# Salva em CSV
df_top20 = pd.DataFrame(top20, columns=["kmer", "frequencia"])
df_top20.to_csv("Asfaviridae_top20_kmers.csv", index=False)

print("\nSalvo como 'Poxviridae_top20_kmers.csv'")
