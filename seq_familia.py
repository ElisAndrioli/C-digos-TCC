#quantas sequências existem em cada arquivo .fasta 

import glob #localizar todos os arquivos .fasta 

# Encontra todos os arquivos .fasta na pasta
arquivos_fasta = glob.glob("*.fasta")

# Abre o arquivo de saída para escrita
with open("quantidade_sequencias.txt", "w") as saida:
    for arquivo in arquivos_fasta:
        with open(arquivo, 'r') as f:
            # Conta quantas linhas começam com '>'
            num_sequencias = sum(1 for linha in f if linha.startswith('>'))
        # Escreve o resultado no arquivo
        saida.write(f"{arquivo}: {num_sequencias} sequências\n")

print("Arquivo 'quantidade_sequencias.txt' gerado com sucesso!")

