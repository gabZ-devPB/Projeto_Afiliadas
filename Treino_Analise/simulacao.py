import pandas as pd
import numpy as np

df_afiliadas = pd.read_csv('Arquivos/afiliadas.csv')
df_afiliadas['Lucro_R$'] = df_afiliadas['Receita_R$'] - df_afiliadas['Custo_R$']
df_afiliadas['ROI(%)'] = (df_afiliadas['Lucro_R$'] / df_afiliadas['Custo_R$']) * 100
df_afiliadas['Taxa_Conversao'] = df_afiliadas['Conversoes'] / df_afiliadas['Cliques']

df_simulado = df_afiliadas.copy()

# Crescimento de investimento (5% a 30%)

df_simulado['Fator_Crescimento'] = np.random.uniform(1.05, 1.30, len(df_simulado))

df_simulado['Cliques'] = (df_simulado['Cliques'] * df_simulado['Fator_Crescimento']).astype(int)
df_simulado['Custo_R$'] = (df_simulado['Custo_R$'] * df_simulado['Fator_Crescimento']).round(2)

# Variação de conversão (-10% a +15%)

df_simulado['Fator_Conversao'] = np.random.uniform(0.90, 1.15, len(df_simulado))
df_simulado['Conversoes'] = (
    df_simulado['Conversoes'] * df_simulado['Fator_Conversao']
).astype(int)

# Garantir consistência

df_simulado['Conversoes'] = df_simulado[['Cliques','Conversoes']].min(axis=1)


# 5. RECALCULAR MÉTRICAS

ticket_medio = df_afiliadas['Receita_R$'] / df_afiliadas['Conversoes']
ticket_medio = ticket_medio.replace([np.inf, -np.inf], 0).fillna(0)

df_simulado['Receita_R$'] = (df_simulado['Conversoes'] * ticket_medio).round(2)
df_simulado['Lucro_R$'] = df_simulado['Receita_R$'] - df_simulado['Custo_R$']
df_simulado['ROI(%)'] = (df_simulado['Lucro_R$'] / df_simulado['Custo_R$']) * 100
df_simulado['Taxa_Conversao'] = df_simulado['Conversoes'] / df_simulado['Cliques']


# 6. COMPARAÇÃO ANTES x DEPOIS

df_comparacao = pd.DataFrame({
    'Afiliada': df_afiliadas['Afiliada'],
    'ROI_Atual': df_afiliadas['ROI(%)'],
    'ROI_Simulado': df_simulado['ROI(%)'],
    'Delta_ROI': df_simulado['ROI(%)'] - df_afiliadas['ROI(%)'],
    'Lucro_Atual': df_afiliadas['Lucro_R$'],
    'Lucro_Simulado': df_simulado['Lucro_R$']
})

df_comparacao.to_csv('simulacao/comparacao.csv')
df_simulado.to_csv('simulacao/simulacao.csv')
