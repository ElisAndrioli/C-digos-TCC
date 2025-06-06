#Em quantas sequências da mesma família esse k-mer aparece pelo menos uma vez?
#repetição dos kerms mais comuns entre as sequencias das familias 

import pandas as pd
import glob
from Bio import SeqIO

# Encontra todos os arquivos *_top20_kmers.csv
arquivos_kmers = glob.glob("*_top20_kmers.csv")

for arquivo_kmer in arquivos_kmers:
    familia = arquivo_kmer.replace("_top20_kmers.csv", "")
    arquivo_fasta = f"{familia}.fasta"

    # Lê os top 20 kmers da família
    df_kmers = pd.read_csv(arquivo_kmer)
    kmers = df_kmers['kmer'].astype(str).str.upper().tolist()

    # Lê as sequências do arquivo .fasta
    sequencias = [str(record.seq).upper() for record in SeqIO.parse(arquivo_fasta, "fasta")]
    print(f"{familia}: {len(sequencias)} sequências no total")


    resultados = []

    for kmer in kmers:
        # Conta em quantas sequências esse k-mer aparece ao menos uma vez
        ocorrencias = sum(1 for seq in sequencias if kmer in seq)
        resultados.append({ "kmer": kmer, "n_sequencias_com_esse_kmer": ocorrencias})


    # Salva em CSV por família
    df_resultado = pd.DataFrame(resultados)
    df_resultado.to_csv(f"{familia}_kmers_em_cada_sequenciasDaFamilia.csv", index=False)    
    print(f"Salvo: {familia}_kmers2_em_cada_sequenciasDaFamilia.csv")
