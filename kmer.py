from Bio import SeqIO # ler e escrever arquivos de sequências biológicas 
from collections import Counter #contar a ocorrência de itens em um iterável -> qunatas vezes o K aparece
import pandas as pd #manipulaçao de dados e tabelas -> armazenar o perfil de K-mers em um DF e depois exporta como um arquivo CSV
import itertools #cria iteradores eficientes (product)
#import sys #interagir com o sistema operacional


#Função que retorna uma lista com todos os K-mers presentes na sequência
#seq: sequência de DNA
#k = comprimento k
def get_kmers(seq, k):
    #começa na posição i -> i percorre a sequência extraindo K-mers a partir de cada posição até o final
    return [seq[i:i+k] for i in range(len(seq) - k + 1)] #vai do i ate o i+k = final da sequencia


#função que gera todos os possíveis K-mers para o valor de k
#cada K-mer é composto por combinações de A, C, G, T -> nucleotídeos
def all_possible_kmers(k):
    #product -> gera o produto cartesiano dos nucleotídeos 'A', 'C', 'G' e 'T'.
    #repeat=k -> o produto será feito para criar todas as combinações possíveis de k elementos 
    #join transforma os K-mers do em string
    return [''.join(p) for p in itertools.product('ACGT', repeat=k)]


#Funçao gera o perfil de K-mers a partir de um arquivo FASTA
def kmer_profile(fasta_file, k):
    profiles = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        kmers = get_kmers(str(record.seq).upper(), k)
        counter = Counter(kmers)
        profiles[record.id] = counter
    return profiles



#função salva o perfil de K-mers em um arquivo CSV
def save_profile(profiles, k, output_csv):
    kmers = all_possible_kmers(k)
    df = pd.DataFrame.from_dict(profiles, orient='index')
    df = df.reindex(columns=kmers, fill_value=0)
    df.to_csv(output_csv)






