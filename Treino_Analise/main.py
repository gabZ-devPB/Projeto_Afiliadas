import pandas as pd

df_afiliadas = pd.read_csv('Arquivos/afiliadas.csv')

# Criacao de colunas novas

df_afiliadas['Taxa_Conversao(%)'] = (df_afiliadas['Conversoes'] / df_afiliadas['Cliques']) * 100
df_afiliadas['Lucro_R$'] = df_afiliadas['Receita_R$'] - df_afiliadas['Custo_R$']
df_afiliadas['ROI(%)'] = (df_afiliadas['Lucro_R$'] / df_afiliadas['Custo_R$']) * 100

# Qual Afiliada tem o maior ROI
# Mostra em ordem decrescente o ROI de cada Afiliada:
# Mostra o TOP 5 Afiliadas por ROI
# Mostra o TOP 5 Afiliadas por Lucro

Lucro_afiliadas = df_afiliadas.groupby('Afiliada')['Lucro_R$'].max().reset_index().sort_values(by='Lucro_R$', ascending=False)
ROI_afiliadas = df_afiliadas.groupby('Afiliada')['ROI(%)'].max().reset_index().sort_values(by='ROI(%)', ascending=False)

TOP_5_Lucro_afiliadas = Lucro_afiliadas.head()
TOP_5_ROI_afiliadas = ROI_afiliadas.head()

# Afiliadas que devem ser pausadas
# Devem ser pausadas quando:
    # ❌ Lucro negativo
    # ❌ ROI < 0%
    # ❌ Conversão < 1%
    # ❌ Custo por conversão > ticket
    # ❌ Muito gasto sem retorno
    # Se tiver menos de 50 Cliques e considerado teste

df_afiliadas['Pausar'] = (
    (df_afiliadas['Lucro_R$'] < 0) | 
    (df_afiliadas['ROI(%)'] < 0) |
    ((df_afiliadas['Conversoes'] / df_afiliadas['Cliques']) < 0.01) &
    (df_afiliadas['Cliques'] > 50)
)
Pausar = df_afiliadas[df_afiliadas['Pausar'] == True]

Pausar.to_csv('analise/Pausar_Afilidas.csv')
Lucro_afiliadas.to_csv('analise/Lucro_por_afilidadas.csv')
ROI_afiliadas.to_csv('analise/Roi_por_afilidadas.csv')
TOP_5_ROI_afiliadas.to_csv('analise/TOP 5_afiliadas_ROI.csv')
TOP_5_Lucro_afiliadas.to_csv('analise/TOP 5_afiliadas_Lucro.csv')