# -*- coding: utf-8 -*-
"""ListaExercicio4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KWPG90SzY2IaPi7nSV45_m4r0bIhkpe

# 📊 Projeto Final – Análise Contábil com Ajuste Econômico

Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.

1) Configure o título na barra do navegador, da página do projeto no Streamlit e descrição inicial do projeto (peso: 1,0)

- Título na barra (`page_title`): Lista de Exercícios 4
- Título da página (`header`): Projeto Final – Análise Contábil com Ajuste Econômico
- Descrição projeto (`write`): Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.
"""


import streamlit as st

st.set_page_config(
    page_title="Lista de Exercícios 4",
    page_icon="📊",
)
st.header("Projeto Final – Análise Contábil com Ajuste Econômico")
st.write("Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.")

"""2) Importe os dados do arquivo empresas_dados.csv utilizando pandas e apresente todas as linhas da df (peso: 1,0)

Dica: Utilize `head(len(df))`
"""

import pandas as pd

df = pd.read_csv("empresas_dados.csv", sep=';')
st.dataframe(df.head(len(df)))

"""3) Calcule os indicadores Margem Líquida e ROA e salve como novas coluna da df. Depois apresente os dois indicadores no mesmo gráfico de linhas, agrupado por Ano  (peso: 1,0)

- Margem Líquida = Lucro Líquido / Receita Líquida * 100
- ROA = Lucro Líquido / Ativo Total *  100
"""

import matplotlib.pyplot as plt

df['Margem_Liquida'] = (df['Lucro Líquido'] / df['Receita Líquida']) * 100
df['ROA'] = (df['Lucro Líquido'] / df['Ativo Total']) * 100

df_agrupado = df.groupby('Ano')[['Margem_Liquida', 'ROA']].mean().reset_index()

st.dataframe(df)
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(df_agrupado['Ano'], df_agrupado['Margem_Liquida'], marker='o', label='Margem Líquida')
ax.plot(df_agrupado['Ano'], df_agrupado['ROA'], marker='s', label='ROA')

ax.set_title('Margem Líquida e ROA por Ano')
ax.set_xlabel('Ano')
ax.set_ylabel('%')
ax.grid(True)
fig.tight_layout()
st.pyplot(fig)

"""4) Utilize o pacote ipeadatapy e faça busca para encontrar o indicador que traga o IPCA, taxa de variação, em % e anual: (peso: 2,0)

- Baixe os dados no período de 2010 a 2024
- Altere o nome da coluna "YEAR" para "Ano"
- Altere o nome da coluna "VALUE ((% a.a.))" para "IPCA"
- Apresente a df para checar se tudo deu certo
"""
import ipeadatapy as ip


df_ipca = ip.timeseries('PRECOS_IPCAG', yearGreaterThan=2009, yearSmallerThan=2025)

df_ipca = df_ipca.rename(columns={
    'YEAR': 'Ano',
    "VALUE ((% a.a.))": 'IPCA'
})

st.dataframe(df_ipca.head())


"""5) Combine as duas df (Excel e IPEA) em uma nova df e calcule nova coluna chamada Receita Real (peso: 2,0)

- Utilize a função `pd.merge()` para unificar as duas df utiilizando a coluna Ano como conexão (chave primária) entre elas
- Crie nova coluna chamada Receita Real que será o resultado da Receita Líquida de cada ano deduzido o IPCA do ano: `Receita Real = Receitta Líquida - ( Receita Líquida * (IPCA/100) )`
- Apresente a nova df combinada

"""

receita_real = pd.merge(df, df_ipca, on='Ano')
receita_real['Receita Real'] = receita_real['Receita Líquida'] - (receita_real['Receita Líquida'] * (receita_real['IPCA'] / 100))

st.dataframe(receita_real.head())

"""6) Crie gráfico de linha que apresente as variáveis Receita Líquida e Receita Real ao longo dos anos (no mesmo gráfico) (peso: 1,0)"""

receita_agrupada_por_ano = receita_real.groupby('Ano')[['Receita Líquida', 'Receita Real']].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(receita_agrupada_por_ano['Ano'], receita_agrupada_por_ano['Receita Líquida'], marker='o', label='Receita Líquida')
ax.plot(receita_agrupada_por_ano['Ano'], receita_agrupada_por_ano['Receita Real'], marker='s', label='Receita Real')

ax.set_title('Receita Líquida e Receita Real por Ano')
ax.set_xlabel('Ano')
ax.set_ylabel('Valor')
ax.legend()
ax.grid(True)
fig.tight_layout()

st.pyplot(fig)

"""7) Faça os ajustes necessários e leve este projeto para a web usando GitHub e Streamlit (peso: 2,0)

- Caça os ajustes necessários no projeto para ser publicado no Streamlit
- Crie novo repositório público no GitHub e leve os arquivos .py e .csv pra lá. Aproveite e crie o arquivo requirements.txt com os pacotes utilizados no projeto
- Crie novo projeto no Streamlit e associe ao repositório da lista
"""
