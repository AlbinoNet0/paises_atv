import pandas as pd
from funcoes import *

nome_arq = '2020-2025.csv'
pd.set_option('display.float_format', lambda x: '%.2f' % x)

dados_ranking = ranking(nome_arq)
maioPercentual = maior_percentual_pib(nome_arq)


print("--- Ranking Top 10 Maiores PIBs (Projeção 2025) ---")
print(dados_ranking.to_string(index=False))

print("\n")
maioPercentual['Crescimento_Percentual'] = maioPercentual['Crescimento_Percentual'].map('{:.2f}%'.format)
maioPercentual.insert(0, 'Rank', range(1, 1 + len(maioPercentual)))
print(maioPercentual.to_string(index=False))