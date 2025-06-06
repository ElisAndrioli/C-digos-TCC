# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Carrega o CSV
# df = pd.read_csv("kmer2_ocorrencias_com_nome_familias.csv")

# # Converte a coluna 'familias' em listas
# df['familias'] = df['familias'].str.split(';')

# # Filtra para kmers com ocorrência em duas ou mais famílias
# df['num_familias'] = df['familias'].apply(len)
# df_multi = df[df['num_familias'] > 1]

# # --------- GRÁFICO 1: BARRAS (kmer x número de famílias) ---------
# # plt.figure(figsize=(10, 6))
# # top_kmers = df_multi.sort_values('num_familias', ascending=False)
# # plt.bar(top_kmers['kmer'], top_kmers['num_familias'], color='skyblue')
# # plt.xticks(rotation=90, fontsize=8)
# # plt.xlabel("K-mers")
# # plt.ylabel("Número de Famílias")
# # plt.title("K-mers presentes em mais de uma família")
# # plt.tight_layout()
# # plt.show()

# # --------- GRÁFICO 2: HEATMAP (kmer x famílias) ---------
# # Expande para matriz de presença/ausência
# all_familias = sorted(set(f for familias in df_multi['familias'] for f in familias))
# heatmap_df = pd.DataFrame(0, index=df_multi['kmer'], columns=all_familias)

# for _, row in df_multi.iterrows():
#     for fam in row['familias']:
#         heatmap_df.loc[row['kmer'], fam] = 1

# # Desenha o heatmap
# plt.figure(figsize=(14, max(6, len(heatmap_df) * 0.3)))
# sns.heatmap(heatmap_df, cmap='YlGnBu', cbar_kws={'label': 'Presença'}, linewidths=0.2, linecolor='gray')
# plt.title("Presença de K-mers por Família (apenas K-mers compartilhados)")
# plt.xlabel("Famílias")
# plt.ylabel("K-mers")
# plt.tight_layout()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configura o estilo do seaborn com fundo branco
sns.set(style="white")

# Carrega o CSV
df = pd.read_csv("kmer2_ocorrencias_com_nome_familias.csv")

# Converte a coluna 'familias' em listas
df['familias'] = df['familias'].str.split(';')

# Filtra para kmers com ocorrência em duas ou mais famílias
df['num_familias'] = df['familias'].apply(len)
df_multi = df[df['num_familias'] > 1]

# Cria a matriz presença/ausência
all_familias = sorted(set(f for familias in df_multi['familias'] for f in familias))
heatmap_df = pd.DataFrame(0, index=df_multi['kmer'], columns=all_familias)

for _, row in df_multi.iterrows():
    for fam in row['familias']:
        heatmap_df.loc[row['kmer'], fam] = 1

# Define o tamanho da figura proporcional ao número de k-mers
plt.figure(figsize=(16, max(8, len(heatmap_df) * 0.4)))

# Desenha o heatmap com uma paleta de maior contraste
sns.heatmap(
    heatmap_df,
    cmap='magma_r',  # ou use 'Blues' se preferir
    cbar_kws={'label': 'Presença'},
    linewidths=0.1,
    linecolor='gray',
    xticklabels=True,
    yticklabels=True
)

# Estética dos rótulos e título
plt.title("Presença de K-mers por Família (apenas K-mers compartilhados)", fontsize=14, pad=20)
plt.xlabel("Famílias", fontsize=12)
plt.ylabel("K-mers", fontsize=12)

# Rotaciona e ajusta os rótulos do eixo X
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=9)

# Ajusta layout para não cortar texto
plt.tight_layout()

# (Opcional) Salvar em alta resolução
# plt.savefig("heatmap_kmers_melhorado.png", dpi=300)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo limpo
sns.set(style="white")

# Carrega o CSV
df = pd.read_csv("kmer2_ocorrencias_com_nome_familias.csv")
df['familias'] = df['familias'].str.split(';')
df['num_familias'] = df['familias'].apply(len)
df_multi = df[df['num_familias'] > 1]

# Cria matriz presença/ausência
all_familias = sorted(set(f for familias in df_multi['familias'] for f in familias))
heatmap_df = pd.DataFrame(0, index=df_multi['kmer'], columns=all_familias)
for _, row in df_multi.iterrows():
    for fam in row['familias']:
        heatmap_df.loc[row['kmer'], fam] = 1

# Cria figura com controle de espaço
fig, ax = plt.subplots(figsize=(16, max(8, len(heatmap_df) * 0.4)))

sns.heatmap(
    heatmap_df,
    cmap='magma_r',  # ou 'Blues'
    cbar_kws={'label': 'Presença'},
    linewidths=0.1,
    linecolor='gray',
    xticklabels=True,
    yticklabels=True,
    ax=ax
)

# Título e eixos com fontes maiores
ax.set_title("Presença de K-mers por Família (apenas K-mers compartilhados)", fontsize=16, pad=30)
ax.set_xlabel("Famílias", fontsize=13)
ax.set_ylabel("K-mers", fontsize=13)

# Rotaciona rótulos do eixo X com espaço
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=9)

# Ajusta espaços manuais (em vez de tight_layout)
plt.subplots_adjust(left=0.15, bottom=0.25, top=0.9, right=0.95)

plt.show()


# (Opcional) Sa



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from io import StringIO

# # Dados CSV fornecidos pelo usuário
# csv_data = """
# kmer,ocorrencias,familias
# AAAAAA,11,Adenoviridae;Adintoviridae;Alloherpesviridae;Anelloviridae;Asfaviridae;Genomoviridae;Iridoviridae;Papilomaviridae;Parvoviridae;Polyomaviridae;Poxviridae
# TTTTTT,9,Adenoviridae;Adintoviridae;Alloherpesviridae;Asfaviridae;Circoviridae;Iridoviridae;Papilomaviridae;Polyomaviridae;Poxviridae
# ATTTTT,6,Adintoviridae;Asfaviridae;Iridoviridae;Papilomaviridae;Polyomaviridae;Poxviridae
# TAAAAA,6,Adenoviridae;Adintoviridae;Asfaviridae;Iridoviridae;Papilomaviridae;Polyomaviridae
# AAAAAT,5,Adintoviridae;Anelloviridae;Asfaviridae;Iridoviridae;Poxviridae
# TATTTT,5,Asfaviridae;Iridoviridae;Papilomaviridae;Polyomaviridae;Poxviridae
# TTAAAA,5,Adintoviridae;Asfaviridae;Iridoviridae;Papilomaviridae;Polyomaviridae
# TTTAAA,5,Adintoviridae;Asfaviridae;Iridoviridae;Papilomaviridae;Parvoviridae
# AAAATA,4,Adintoviridae;Asfaviridae;Iridoviridae;Poxviridae
# NNNNNN,4,Adenoviridae;Papilomaviridae;Parvoviridae;Poxviridae
# CAAAAA,4,Anelloviridae;Genomoviridae;Parvoviridae;Polyomaviridae
# TTTTTA,4,Asfaviridae;Iridoviridae;Papilomaviridae;Poxviridae
# TTTTAT,4,Asfaviridae;Circoviridae;Papilomaviridae;Poxviridae
# AATTTT,3,Adintoviridae;Asfaviridae;Iridoviridae
# AAATTT,3,Adintoviridae;Asfaviridae;Iridoviridae
# AGAAAA,3,Adintoviridae;Anelloviridae;Polyomaviridae
# AAAAGA,3,Anelloviridae;Iridoviridae;Parvoviridae
# AAGAAA,3,Adintoviridae;Anelloviridae;Circoviridae
# ATAAAA,3,Adintoviridae;Asfaviridae;Poxviridae
# AAAATT,3,Adintoviridae;Asfaviridae;Iridoviridae
# AAATAT,3,Adintoviridae;Asfaviridae;Poxviridae
# AAAACA,3,Adintoviridae;Anelloviridae;Parvoviridae
# GAAAAA,3,Adintoviridae;Anelloviridae;Asfaviridae
# ATATTT,3,Papilomaviridae;Polyomaviridae;Poxviridae
# ACAACA,2,Anelloviridae;Parvoviridae
# AAACAA,2,Anelloviridae;Parvoviridae
# CAGCAG,2,Adenoviridae;Alloherpesviridae
# AAAGAA,2,Anelloviridae;Circoviridae
# CAACAA,2,Genomoviridae;Parvoviridae
# CCACCA,2,Adenoviridae;Alloherpesviridae
# AGCAGC,2,Adenoviridae;Alloherpesviridae
# AAAAAC,2,Anelloviridae;Polyomaviridae
# AAAAAG,2,Anelloviridae;Polyomaviridae
# GCGGCG,2,Adenoviridae;Alloherpesviridae
# AAGAAG,2,Anelloviridae;Circoviridae
# GCTGCT,2,Alloherpesviridae;Polyomaviridae
# GAAGAA,2,Anelloviridae;Circoviridae
# AACAAA,2,Anelloviridae;Parvoviridae
# AGGAGG,2,Adenoviridae;Circoviridae
# GGAGGA,2,Adenoviridae;Circoviridae
# TTTTAA,2,Asfaviridae;Iridoviridae
# GAGGAG,2,Adenoviridae;Alloherpesviridae
# TATATA,2,Papilomaviridae;Poxviridae
# GGCGGC,2,Adenoviridae;Alloherpesviridae
# ACCACC,2,Adenoviridae;Alloherpesviridae
# GGAAGA,2,Adenoviridae;Circoviridae
# ATATAT,2,Papilomaviridae;Poxviridae
# TGAAAA,2,Adintoviridae;Parvoviridae
# """

# # Carrega CSV em DataFrame
# df = pd.read_csv(StringIO(csv_data))
# df['familias'] = df['familias'].str.split(';')
# df['num_familias'] = df['familias'].apply(len)
# df_multi = df[df['num_familias'] > 1]

# # Criação da matriz presença/ausência
# all_familias = sorted(set(f for familias in df_multi['familias'] for f in familias))
# heatmap_df = pd.DataFrame(0, index=df_multi['kmer'], columns=all_familias)
# for _, row in df_multi.iterrows():
#     for fam in row['familias']:
#         heatmap_df.loc[row['kmer'], fam] = 1

# # Estilo e figura
# sns.set(style="white")
# fig, ax = plt.subplots(figsize=(16, max(8, len(heatmap_df) * 0.4)))

# sns.heatmap(
#     heatmap_df,
#     cmap='magma_r',
#     cbar_kws={'label': 'Presença'},
#     linewidths=0.1,
#     linecolor='gray',
#     xticklabels=True,
#     yticklabels=True,
#     ax=ax
# )

# # Título e ajustes
# ax.set_title("Presença de K-mers por Família (apenas K-mers compartilhados)", fontsize=16, pad=30)
# ax.set_xlabel("Famílias", fontsize=13)
# ax.set_ylabel("K-mers", fontsize=13)
# plt.xticks(rotation=45, ha='right', fontsize=10)
# plt.yticks(fontsize=9)
# plt.subplots_adjust(left=0.15, bottom=0.35, top=0.9, right=0.95)

# plt.savefig("heatmap_kmers_familias.png", dpi=300, bbox_inches='tight')


# plt.show()


