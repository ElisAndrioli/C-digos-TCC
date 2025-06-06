# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Estilo limpo
# sns.set(style="white")

# # Carrega o CSV
# df = pd.read_csv("kmer2_ocorrencias_com_nome_familias.csv")
# df['familias'] = df['familias'].str.split(';')
# df['num_familias'] = df['familias'].apply(len)
# df_multi = df[df['num_familias'] > 1]

# # Agrupa e ordena por número de famílias (descendente)
# df_multi_sorted = df_multi.sort_values('num_familias', ascending=False).reset_index(drop=True)

# # Cria matriz presença/ausência
# all_familias = sorted(set(f for familias in df_multi_sorted['familias'] for f in familias))
# heatmap_df = pd.DataFrame(0, index=df_multi_sorted['kmer'], columns=all_familias)

# for idx, row in df_multi_sorted.iterrows():
#     for fam in row['familias']:
#         heatmap_df.loc[row['kmer'], fam] = 1

# # Índices dos separadores entre grupos de diferentes tamanhos de famílias
# group_breaks = []
# previous_count = df_multi_sorted.loc[0, 'num_familias']
# for i, count in enumerate(df_multi_sorted['num_familias']):
#     if count != previous_count:
#         group_breaks.append(i)
#         previous_count = count

# # Figura
# fig, ax = plt.subplots(figsize=(16, max(8, len(heatmap_df) * 0.4)))

# sns.heatmap(
#     heatmap_df,
#     cmap='magma_r',  # ou 'Blues'
#     cbar_kws={'label': 'Presença'},
#     linewidths=0.1,
#     linecolor='gray',
#     xticklabels=True,
#     yticklabels=True,
#     ax=ax
# )

# # Linhas separando grupos de acordo com número de famílias
# for break_idx in group_breaks:
#     ax.hlines(break_idx, *ax.get_xlim(), colors='white', linewidth=2)

# # Título e eixos
# ax.set_title("Presença de K-mers por Família\n(Agrupado por número de famílias compartilhadas)", fontsize=16, pad=30)
# ax.set_xlabel("Famílias", fontsize=13)
# ax.set_ylabel("K-mers", fontsize=13)

# # Rótulos
# plt.xticks(rotation=45, ha='right', fontsize=10)
# plt.yticks(fontsize=9)

# # Ajuste de layout
# plt.subplots_adjust(left=0.15, bottom=0.25, top=0.88, right=0.95)

# # Exibe
# plt.show()


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

# Agrupa por número de famílias e ordena
df_multi_sorted = df_multi.sort_values(by=['num_familias', 'kmer'], ascending=[False, True]).reset_index(drop=True)

# Cria matriz presença/ausência
all_familias = sorted(set(f for fams in df_multi_sorted['familias'] for f in fams))
heatmap_df = pd.DataFrame(0, index=df_multi_sorted['kmer'], columns=all_familias)
for i, row in df_multi_sorted.iterrows():
    for f in row['familias']:
        heatmap_df.loc[row['kmer'], f] = 1

# Agrupamento com rótulo novo no eixo Y
new_index_labels = []
group_breaks = []
prev_count = None
for i, (kmer, n) in enumerate(zip(df_multi_sorted['kmer'], df_multi_sorted['num_familias'])):
    if n != prev_count:
        new_index_labels.append(f"🔹 {n} famílias\n{kmer}")
        group_breaks.append(i)
        prev_count = n
    else:
        new_index_labels.append(kmer)

heatmap_df.index = new_index_labels

# Plot
fig, ax = plt.subplots(figsize=(16, max(8, len(heatmap_df) * 0.4)))

sns.heatmap(
    heatmap_df,
    cmap='magma_r',
    cbar_kws={'label': 'Presença'},
    linewidths=0.1,
    linecolor='gray',
    xticklabels=True,
    yticklabels=True,
    ax=ax
)

# Linhas brancas entre grupos
for i in group_breaks[1:]:
    ax.hlines(i, *ax.get_xlim(), colors='white', linewidth=2)

# Títulos e eixos
ax.set_title("Presença de K-mers por Família\nAgrupado por número de famílias compartilhadas", fontsize=16, pad=30)
ax.set_xlabel("Famílias", fontsize=13)
ax.set_ylabel("K-mers (agrupados por número de famílias)", fontsize=13)

# Rótulos e espaçamento
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=9)
plt.subplots_adjust(left=0.23, bottom=0.25, top=0.88, right=0.97)

# 🔽 Salva imagem em alta qualidade
plt.savefig("heatmap_kmers_por_familia2.png", dpi=300, bbox_inches='tight')

plt.show()
