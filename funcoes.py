import pandas as pd
from typing import Optional

def ranking(nome_arq: str, ano: str = '2025', top_n: int = 10) -> Optional[pd.DataFrame]:
    try:
        dados = pd.read_csv(nome_arq)
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{nome_arq}' não foi encontrado.")
        return None

    # COLUNA 2025: DADOS QUE PODEM SER FLOAT, SE NÃO PODE, ENTÃO É CONVERTIDO EM UM VALOR ESPECIAL
    dados[ano] = pd.to_numeric(dados[ano], errors='coerce')
    # REMOVE AS LINHAS QUE CONTENHAM O VALOR ESPECIAL
    dados_limpos = dados.dropna(subset=[ano])

    dados_ordenados = dados_limpos.sort_values(by=ano, ascending=False)
    dados_ranking = dados_ordenados.head(top_n)[['Country', ano]].copy()
    
    dados_ranking.insert(0, 'Rank', range(1, len(dados_ranking) + 1))
    
    # Formata a coluna do PIB com separadores de milhar e 2 casas decimais
    dados_ranking[ano] = dados_ranking[ano].apply(lambda x: f'{x:,.2f}')

    return dados_ranking

def maior_percentual_pib(nome_arquivo):
    try:
        dados = pd.read_csv(nome_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

        # Converter as colunas para numérico, forçando erros a se tornarem NaN
    dados['2020'] = pd.to_numeric(dados['2020'], errors='coerce')
    dados['2025'] = pd.to_numeric(dados['2025'], errors='coerce')

        # Remover linhas onde os valores do PIB de 2020 ou 2025 são inválidos ou 2020 é zero
        # O cálculo envolve divisão, então pib_2020 deve ser maior que zero
    dados_limpo = dados.dropna(subset=['2020', '2025'])
    dados_limpo = dados_limpo[dados_limpo['2020'] > 0]


    # Calcular o percentual de crescimento
    # Fórmula: (((pib_2025 / pib_2020) - 1) * 100)
    dados_limpo['Crescimento_Percentual'] = (
        (dados_limpo['2025'] / dados_limpo['2020']) - 1
    ) * 100

    dados_limpo_10 = dados_limpo.sort_values(by='Crescimento_Percentual', ascending=False).head(10)
    dados_resultado = dados_limpo_10[['Country', 'Crescimento_Percentual']]

    return dados_resultado