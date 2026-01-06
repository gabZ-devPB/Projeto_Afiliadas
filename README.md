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

