# 📊 Simulação e Análise de Afiliadas

Este projeto tem como objetivo realizar **análise de dados e simulação de cenários futuros** a partir de uma base histórica de afiliadas, utilizando **Python, Pandas e NumPy**.

O foco é a **tomada de decisão orientada por dados**, avaliando métricas como **Lucro, ROI e Taxa de Conversão**, além de simular o impacto de aumento de investimento e variação de performance.

---

## 🧠 Objetivo do Projeto

- Calcular métricas de negócio a partir de dados históricos
- Avaliar a performance das afiliadas
- Simular um **cenário futuro (próximo mês)**
- Comparar **cenário atual vs cenário simulado**
- Gerar arquivos CSV prontos para análises e dashboards

---

## 🗂 Estrutura do Projeto

📁 Treino_Analise
│
├── 📁 Arquivos
│ └── afiliadas.csv
│
├── 📁 simulacao
│ ├── simulacao.csv
│ └── comparacao.csv
│
├── 📁 analise
│ ├── Lucro_por_afiliadas.csv
│ └── Pausar_afiliadas.csv
│ └── Roi_por_afiliadas.csv
│ └── TOP 5_afiliadas_Lucro.csv
│ └── TOP 5_afiliadas_ROI.csv
│
├── simulacao.py
├── main.py
└── README.md
---

## 📥 Entrada de Dados

O projeto utiliza um arquivo CSV contendo dados históricos das afiliadas.

### Colunas esperadas:
- `Afiliada`
- `Cliques`
- `Conversoes`
- `Receita_R$`
- `Custo_R$`

---

## 📊 Análise Estratégica

Nesta etapa do projeto foi realizada a **engenharia de métricas**, criando indicadores essenciais para avaliação de performance das afiliadas.

### 📊 Métricas criadas

#### 🔄 Taxa de Conversão (%)
Indica a eficiência da afiliada em transformar cliques em vendas.

#### 💰 Lucro (R$)
Representa o ganho real após descontar os custos.

#### 📈 ROI (%)
Mede a eficiência do investimento realizado.

Essas métricas são fundamentais para análises de negócio e tomadas de decisão estratégicas.

---

Com base nas métricas calculadas, foi realizada uma **análise estratégica das afiliadas**, focada em performance e rentabilidade.

### 🏆 Top 5 afiliadas por ROI
Identificação das afiliadas com **maior eficiência de investimento**, ou seja, aquelas que geram mais retorno proporcional ao custo.

Critério:
- Ordenação decrescente por **ROI (%)**
- Seleção das 5 melhores afiliadas

---

### 💵 Top 5 afiliadas por Lucro
Identificação das afiliadas que geram **maior lucro absoluto**, independentemente do ROI.

Critério:
- Ordenação decrescente por **Lucro_R$**
- Seleção das 5 afiliadas mais lucrativas

---

### 🚫 Afiliadas que devem ser pausadas
Foram identificadas afiliadas que apresentam **performance negativa ou abaixo do esperado**, com base nos seguintes critérios:

- **Lucro negativo**
- **ROI inferior a 0%**
- **Baixa taxa de conversão**

Essas afiliadas são classificadas como candidatas a **pausa ou otimização**, evitando prejuízos e melhorando a alocação de recursos.

---

## 🧠 Insight de Negócio

A análise demonstra que **alto faturamento não significa necessariamente alto lucro**, reforçando a importância do uso de métricas como ROI e Taxa de Conversão para decisões mais eficientes.

O projeto evidencia uma abordagem orientada a dados, simulando cenários reais de análise de performance no contexto de marketing de afiliados.

## 📊 Métricas Calculadas

As métricas abaixo são calculadas automaticamente pelo código:

Essas métricas são calculadas tanto para a **base histórica** quanto para os **dados simulados**.

---

## 🔮 Simulação de Cenário Futuro

A simulação representa o **próximo período**, aplicando:

### 📈 Crescimento de investimento
- Aumento de cliques e custos entre **5% e 30%**

### 🔄 Variação de conversão
- Alteração da taxa de conversão entre **-10% e +15%**

### 🔁 Recalculo completo
Após a simulação, todas as métricas são recalculadas para garantir **consistência dos dados**.

---

## 📉 Comparação de Cenários

É gerado um DataFrame comparando:

- ROI atual vs ROI simulado
- Lucro atual vs lucro simulado
- Variação do ROI (Delta)

---

## 📤 Arquivos Gerados

### 📄 `simulacao/simulacao.csv`
Contém os dados simulados do próximo período, incluindo:
- Cliques
- Conversões
- Receita
- Custo
- Lucro
- ROI
- Taxa de Conversão

### 📄 `simulacao/comparacao.csv`
Contém a comparação direta entre:
- Cenário atual
- Cenário simulado

---

## 🛠 Tecnologias Utilizadas

- **Python**
- **Pandas**
- **NumPy**

---

