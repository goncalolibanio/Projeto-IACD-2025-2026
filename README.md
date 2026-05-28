🥗 Previsão do Sucesso de Dietas - Machine Learning

Este repositório contém o trabalho prático final da Unidade Curricular de Elementos de Inteligência Artificial e Ciência de Dados da Universidade da Beira Interior (UBI) - Ano Letivo 2025/2026.

👥 Equipa:
Caio Santos (Nº 55791)
Eva Trindade (Nº 56600)
Gonçalo Libânio (Nº 55925)

🎯 Objetivo do Projeto:
O sucesso de um plano alimentar depende de uma teia complexa de fatores biológicos, comportamentais e clínicos. O objetivo principal deste projeto é aplicar técnicas avançadas de Análise Exploratória, Limpeza de Dados, Clustering e Modelação Preditiva (Machine Learning) para estimar a perda de peso de um paciente num horizonte de 6 meses (weight_change_kg_6m).

📊 Conjunto de Dados (Dataset)

O projeto baseia-se na integração de quatro ficheiros CSV originais:

patients.csv (Idade, IMC, Peso Base, etc.)
diets.csv (Tipo de dieta: Low Carb, Balanced, High Protein)
nutritionists.csv (Anos de experiência, Especialidade, Abordagem)
outcomes.csv (Resultados reais ao fim de 6 meses)

Através do script read_data.py, os dados foram consolidados (Left Joins) num único conjunto unificado composto por 2523 instâncias e 31 variáveis.

⚙️ Pipeline de Desenvolvimento

1. Pré-Processamento de Dados (data_processing.py)

Limpeza: Remoção de variáveis redundantes ou linearmente dependentes (ex: total_macros).
Tratamento de Nulls: Imputação de dados em falta utilizando medianas, médias globais e médias agrupadas por contexto (ex: por tipo de dieta).
Tratamento de Outliers: Aplicação do método do Intervalo Interquartil (IQR) e Clipping para limites fisiologicamente plausíveis.

Análise Exploratória (EDA):

Exploração univariada e bivariada das características biológicas e comportamentais. A Matriz de Correlação revelou que variáveis comportamentais (mean_adherence_pct, motivation_score) possuem correlações lineares consideravelmente mais fortes com o sucesso da dieta do que fatores biológicos isolados (como age ou sleep_hours).

Aprendizagem Não Supervisionada (Clustering):

Aplicação do algoritmo K-Means, com o k ótimo determinado pelos métodos do Elbow e Silhouette Score.
Visualização da segmentação de pacientes em perfis através de PCA 2D.
Extração de padrões (ex: Sazonalidade vs. Idade e Perfil do Nutricionista vs. Sexo do Paciente).

Modelação Preditiva (Machine Learning)

Avaliação de modelos supervisionados de regressão para prever a variação de peso, com divisão de dados Train/Test (80/20) e otimização de hiperparâmetros (GridSearch).



Modelo			        RMSE		MAE		  R² Score

Regressão Linear	  3.278		2.325		0.815

Random Forest		    3.366		2.364		0.805

Gradient Boosting	  3.243		2.089		0.819


📂 Estrutura do Repositório

├── data/                   # Pasta com os ficheiros CSV originais (se aplicável/público)
├── scripts/
│   ├── read_data.py        # Script de junção relacional dos datasets
│   └── data_processing.py  # Script de limpeza, clipping e imputação
├── notebooks/
│   └── analise_dietas.ipynb # Notebook principal com EDA, Clusters e ML
├── apresentacao/
│   └── apresentacao_5min_ubi.html # Ficheiro da apresentação final interativa
├── Relatorio_Trabalho_Pratico_IA.pdf # Relatório técnico final
└── README.md               # Este documento


🚀 Como Executar o Projeto:

Abrir o ficheiro e o analysis.ipynb e correr sequencialmente as células do notebook

GERADO COM APOIO DE IA GENERATIVA
