# Restaurant Sales Prediction


## Overview

Este repositório é um protótipo inicial de um modelo de prever as vendas de um restaurante para os próximos 7 dias.

## Quick Start

`demo_quick_start_notebook.ipynb` é um tutorial mostrando todas as etapas de feature engineering, criação e avaliação do modelo.

## Requirements

* **Data:** O app requer apenas o valor total da vendas diárias, como segue esse exemplo:

date | sales | 
--- | --- |
2021-06-01 | 3540.91 |
2021-06-02 | 5049.35 |
2021-06-03 | 7655.55 |
2021-06-04 | 5885.45 |

Contudo, o ideal é que sejam fornecidas as vendas com frequência em horas, para que sejam identificados o fluxo por turnos. Mais informações costumam melhorar a perfomace do modelo. O período ideal mínimo requerido é de ao menos 365 dias.
  
## Outputs

1. **Predicted Daily Sales** é o valor futuro das venda em um determinado dia.

| date | sales | 
| --- | ---|
| 2021-06-01 | 1540.10 |
| 2022-06-02 | 4049.52 |
| 2022-06-03 | 7655.00 |
| 2022-06-04 | 9885.95 |

1. **Daily Daily Demand** é o valor previsto classificado como Low, Normal, High e Peak. A classificação tem como base os valores mínimo e máximo e o percentil 25%, 50% e 75% do valor das vendas do conjunto de treino.

| date | sales | 
| --- | --- |
| 2021-06-01 | Low |
| 2022-06-02 | Normal |
| 2022-06-03 | High |
| 2022-06-04 | Peak |

3. **Data Statistics** mostra um sumário estatístico com informações relevantes sobre o período. Nele são incluídas informações em relação ao tempo e fatores climáticos.

4. **Model Evaluation** resultados dos modelos.
- time_run
- model_id
- mae_normalised
- mape

## Solution description

* **Data cleaning**
* **Build ML data.**
* **Model Training**
* **Model evaluation.**
* **Customer insights.**
* **Predictions & Scheduling.**
* **Monitor feature skew and drift.** 