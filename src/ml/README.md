# Machine Learning - Monitoramento de Máquinas Industriais

Este projeto implementa uma solução de Machine Learning para monitoramento e previsão de falhas em máquinas industriais com base em dados de sensores.

## 🚀 Começando

### Pré-requisitos

- Python 3.8 ou superior
- Git (opcional, para clonar o repositório)
- Ambiente virtual Python (recomendado)

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório (se ainda não tiver feito)
```bash
git clone <git@github.com:Fiap-RJ/Enterprise_Challenge-Sprint_3-Reply.git>
cd Enterprise_Challenge-Sprint_3-Reply/src/ml
```

### 2. Criar e ativar ambiente virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências
```bash
   pip install -r ../../../requirements.txt
```

### 4. Configurar o Jupyter (opcional)
```bash
python3 -m ipykernel install --user --name=venv --display-name="Python (venv)"
```

## 🏃 Pipeline de Machine Learning

Para executar o projeto do início ao fim, siga os passos abaixo no terminal, a partir da pasta `src/ml`.

### Passo 1: Gerar os Dados

Este comando cria os arquivos CSV com dados sintéticos de máquinas, sensores e medições.

```bash
python generate_data.py
```
*Os arquivos serão salvos em `data/raw/`.*

### Passo 2: Executar a Análise Exploratória (EDA)

Este script gera um relatório rápido e salva os gráficos da análise dos dados.

```bash
python run_eda.py
```
*Os gráficos serão salvos em `reports/figures/`.*

### Passo 3: Treinar o Modelo de Machine Learning

Este comando treina um modelo para prever a temperatura, avalia seu desempenho e salva o artefato final.

```bash
python train_model.py
```
*O modelo treinado (`temperature_prediction_model.joblib`) será salvo na pasta `models/`.*

## 📁 Estrutura de Diretórios

```
ml/
├── data/               # Dados brutos e processados
│   ├── raw/           # Dados brutos originais
│   └── processed/     # Dados processados
├── notebooks/         # Jupyter notebooks para análise
├── models/            # Modelos treinados
├── src/               # Código-fonte Python
└── utils/             # Utilitários e funções auxiliares
```

## 📊 Dados Gerados

O script de geração de dados cria 3 conjuntos principais:
1. `maquinas.csv`: Informações sobre as máquinas monitoradas
2. `sensores.csv`: Dados dos sensores instalados
3. `medicoes.csv`: Leituras dos sensores ao longo do tempo

