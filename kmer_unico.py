#kmers que são unicos de cada familia 

import os
from Bio import SeqIO

# Função para gerar todos os k-mers de uma sequência
def gerar_kmers(sequencia, k=6):
    # Retorna um conjunto com todos os k-mers da sequência
    return {sequencia[i:i+k] for i in range(len(sequencia) - k + 1)}

# Parâmetros
k = 6 # Define o tamanho do k-mer
pasta = "C://Users//elisa//OneDrive//Área de Trabalho//NCBI_Vírus" # Caminho da pasta com os arquivos fasta

#Lista todos os arquivos fasta na pasta
arquivos_fasta = [f for f in os.listdir(pasta) if f.endswith(".fasta") or f.endswith(".fa")]

# Indexar todos os k-mers por família, um por vez
print("Indexando todos os k-mers por família...") #para eu saber que familia está sendo processada

# Loop para processar cada família individualmente
for i, arquivo_alvo in enumerate(arquivos_fasta):
    # Extrai o nome da família a partir do nome do arquivo
    # Exemplo: se o arquivo for "Poxviridae.fasta", a família será "Poxviridae" -> mais facil de identificar
    familia_alvo = arquivo_alvo.replace(".fasta", "").replace(".fa", "")
    print(f"\nProcessando família: {familia_alvo}")

    # Obter k-mers da família atual
    kmers_alvo = set() #Inicializa um conjunto para armazenar os k-mers da família atual

    # Para cada sequência no arquivo fasta da família atual
    for registro in SeqIO.parse(os.path.join(pasta, arquivo_alvo), "fasta"):
        seq = str(registro.seq).upper()  # Converte a sequência para maiúsculas
        kmers_alvo.update(gerar_kmers(seq, k))  # Adiciona os k-mers da sequência ao conjunto

    
    outros_kmers = set() # Inicializa um conjunto para armazenar os k-mers das outras famílias

    # Loop para processar os arquivos das outras famílias
    for j, arquivo_outro in enumerate(arquivos_fasta):
        if i == j:
            continue # Pula o arquivo da família atual
        
        # Para cada sequência no arquivo fasta da outra família
        for registro in SeqIO.parse(os.path.join(pasta, arquivo_outro), "fasta"):
            seq = str(registro.seq).upper() # Converte a sequência para maiúsculas
            outros_kmers.update(gerar_kmers(seq, k)) # Adiciona os k-mers ao conjunto


    # Calcula os k-mers exclusivos da família atual (presentes apenas nela)
    exclusivos = kmers_alvo - outros_kmers

    # Salvar em arquivo .txt
    with open(f"{familia_alvo}_kmers_exclusivos.txt", "w") as f:
        f.write(f"Família: {familia_alvo}\n")
        f.write(f"Total de exclusivos: {len(exclusivos)}\n")
        for kmer in sorted(exclusivos): # Escreve cada k-mer exclusivo em ordem alfabética
            f.write(f"{kmer}\n")

    print(f"{len(exclusivos)} k-mers exclusivos salvos em {familia_alvo}_kmers_exclusivos.txt")











 
