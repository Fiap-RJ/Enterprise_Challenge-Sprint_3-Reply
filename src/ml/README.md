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

## 🏃 Executando o Projeto

### 1. Gerar Dados Sintéticos

Para gerar os dados sintéticos, execute o script Python:

```bash
# Navegue até a pasta do projeto
cd src/ml

# Execute o script de geração de dados
python3 generate_data.py
```

#### Arquivos Gerados
Os seguintes arquivos serão criados em `data/raw/`:
- `maquinas.csv`: Informações das máquinas (ID, tipo, modelo, etc.)
- `sensores.csv`: Dados dos sensores (ID, tipo, máquina associada, etc.)
- `medicoes.csv`: Leituras dos sensores (temperatura, umidade, timestamp)

### 2. Análise Exploratória
Após gerar os dados, execute o notebook de análise exploratória:
```bash
jupyter notebook notebooks/02_eda.ipynb
```

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

