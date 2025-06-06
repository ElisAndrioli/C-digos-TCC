import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Encontra todos os arquivos no padrão desejado
arquivos = glob.glob("*_kmers_em_cada_sequenciasDaFamilia.csv")

# Cria uma pasta para salvar as imagens
os.makedirs("Distribuição_kmers_por_seq", exist_ok=True)

# Loop por cada arquivo
for arquivo in arquivos:
    familia = arquivo.replace("_kmers_em_cada_sequenciasDaFamilia.csv", "")
    df = pd.read_csv(arquivo)

    # Ordena por número de sequências em que o k-mer aparece
    df = df.sort_values(by="n_sequencias_com_esse_kmer", ascending=True)

    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    barras = plt.barh(df['kmer'], df['n_sequencias_com_esse_kmer'], color='#b7e1cd')

    # Adiciona os valores no final das barras
    for barra in barras:
        largura = barra.get_width()
        plt.text(largura + max(df['n_sequencias_com_esse_kmer']) * 0.01,
                 barra.get_y() + barra.get_height()/2,
                 f'{int(largura)}', va='center', fontsize=8)

    # Ajustes visuais
    plt.title(f'Distribuição dos K-mers entre as sequências da família - {familia}')
    plt.xlabel('Nº de Sequências com o K-mer')
    plt.ylabel('K-mer')
    plt.tight_layout()

    # Salva imagem
    plt.savefig(f"Distribuição_kmers_por_seq/{familia}_graficoDistribuicao_kmers.png")
    plt.close()

print("Gráficos salvos na pasta 'Distribuição_kmers_por_seq'.")
