#2. Código exemplo para o heatmap + dendrograma
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


# 1. Ler dados
df = pd.read_csv('todos_kmers_exclusivos_com_ocorrencias.csv')

# 2. Criar matriz pivô: famílias x k-mers
matrix = df.pivot(index='familia', columns='kmer_exclusivo', values='n_sequencias_com_esse_kmer').fillna(0)

# 3. Cluster hierárquico nas famílias
linkage_familias = linkage(matrix, method='ward')

# 4. Plot dendrograma
plt.figure(figsize=(40, 20))
dendrogram(linkage_familias, labels=matrix.index, leaf_rotation=90)
plt.title('Dendrograma das Famílias baseado nos k-mers')
plt.show()

# 5. Heatmap com clustering (reordenando linhas pelo dendrograma)
sns.clustermap(matrix, method='ward', metric='euclidean', cmap='viridis', figsize=(15,10))
plt.title('Heatmap de Frequência dos k-mers exclusivos por Família')
plt.show()
