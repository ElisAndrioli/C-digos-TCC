import pandas as pd

# Dados organizados
dados = [
    ["Superfamily 3 Helicase (S3H)", "Poxviridae", "dsDNA"],
    ["Single Jelly Roll (SJR)", "Polyomaviridae", "dsDNA"],
    ["Double Jelly Roll (DJR)", "Circoviridae", "ssDNA"],
    ["Double Jelly Roll (DJR)", "Parvoviridae", "ssDNA"],
    ["Double Jelly Roll (DJR)", "Adenoviridae", "dsDNA"],
    ["RCRE (Rolling Circle Replication Endonuclease)", "Circoviridae", "ssDNA"],
    ["DNA Polymerase Family B", "Herpesviridae", "dsDNA"],
    ["DNA Polymerase Family B", "Iridoviridae", "dsDNA"],
    ["HK97-like Major Capsid Protein", "Alloherpesviridae", "dsDNA (análise desconsiderada)"],
    ["FtsK-like Genome Packaging ATPase", "Adintoviridae", "dsDNA"],
    ["Minor Capsid Protein", "Parvoviridae", "ssDNA"],
    ["Minor Capsid Protein", "Papillomaviridae", "ssDNA"],
    ["Minor Capsid Protein", "Polyomaviridae", "dsDNA"],
    ["Major Capsid Protein", "Poxviridae", "dsDNA"],
    ["Major Capsid Protein", "Adenoviridae", "dsDNA"],
    ["Major Capsid Protein", "Parvoviridae", "ssDNA"],
]

# Cria o DataFrame
df = pd.DataFrame(dados, columns=["Proteína viral", "Família viral", "Tipo de genoma"])

# Salva em CSV
df.to_csv("tabela_proteinas_familias_genoma2.csv", index=False)

print("Tabela salva como 'tabela_proteinas_familias_genoma.csv'")
