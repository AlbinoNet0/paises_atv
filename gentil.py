import pandas as pd

nome_arq = '2020-2025.csv'
pd.set_option('display.float_format', lambda x: '%.2f' % x)

try: 
    dados = pd.read_csv(nome_arq)
except FileNotFoundError:
    print(f"ERRO: O arquivo '{nome_arq}' não foi encontrado.")
    exit()

# COLUNA 2025: DADOS QUE PODEM SER FLOAT, SE NÃO PODE, ENTÃO É CONVERTIDO EM UM VALOR ESPECIAL
dados['2025'] = pd.to_numeric(dados['2025'], errors='coerce')
# REMOVE AS LINHAS QUE CONTENHAM O VALOR ESPECIAL
dados_limpos = dados.dropna(subset=['2025'])

#SELECIONAR O TOP 10 E FORMATAR PARA EXIBIÇÃO
dados_ordenados = dados_limpos.sort_values(by='2025', ascending=False)
dados_ranking = dados_ordenados.head(10)[['Country', '2025']]
dados_ranking['2025'] = dados_ranking['2025'].apply(lambda x: f'{x:,.2f}')


print("--- Ranking Top 10 Maiores PIBs (Projeção 2025) ---")
print(dados_ranking.to_string(index=False))