import json

# Carregando o JSON com os dados de faturamento
with open('dados.json') as f:
    dados_faturamento = json.load(f)

# Criaando uma lista com apenas os valores de faturamento diário, ignorando os dias sem faturamento
valores_faturamento = [dia['valor'] for dia in dados_faturamento if dia['valor'] != 0.0]
print(valores_faturamento)
print(len(valores_faturamento))

# Calculando o menor valor de faturamento diário
menor_valor = min(valores_faturamento)

# Calculando o maior valor de faturamento diário
maior_valor = max(valores_faturamento)

# Calculando a média mensal de faturamento diário, ignorando os dias sem faturamento
media_mensal = sum(valores_faturamento) / len([dia for dia in dados_faturamento if dia['valor'] != 0])

# Contando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

# Imprimir os resultados
print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_da_media)