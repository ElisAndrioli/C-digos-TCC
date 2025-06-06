import matplotlib.pyplot as plt
import pandas as pd

# Dados: nomes das famílias e quantidade de sequências (corrigindo caracteres)
dados = {
    'Família': [
        'Adintoviridae', 'Alloherpesviridae', 'Genomoviridae',
        'Iridoviridae', 'Polyomaviridae', 'Asfaviridae', 'Circoviridae',
        'Parvoviridae', 'Anelloviridae', 'Adenoviridae', 'Papilomaviridae',
        'Poxviridae', 'Herpesviridae'
    ],
    'Sequências': [
        123, 1040, 2101,
        2822, 14673, 14834, 25933,
        36735, 31659, 33096, 47632,
        24726, 71324
    ]
}

# Cria o DataFrame e ordena
df = pd.DataFrame(dados)
df = df.sort_values(by='Sequências')

# Define cor verde clara
cor = '#b7e1cd'

# Criação do gráfico
plt.figure(figsize=(10, 8))
barras = plt.barh(df['Família'], df['Sequências'], color=cor, edgecolor='none')

# Adiciona os valores ao final de cada barra
for barra in barras:
    largura = barra.get_width()
    plt.text(largura + 500, barra.get_y() + barra.get_height()/2,
             f'{int(largura)}', va='center', fontsize=9)

# Personalizações visuais
plt.xlabel("Número de Sequências")
plt.title("Número de Sequências por Família (Ordenado)")
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.gca().spines['left'].set_visible(False)  # remove risquinho preto da esquerda
plt.tight_layout()

plt.show()
