import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

def run_exploratory_analysis():
    """Carrega os dados, realiza a análise exploratória e salva os resultados."""
    print("🚀 Iniciando Análise Exploratória de Dados (EDA)...")

    # --- 1. Carregamento dos Dados ---
    try:
        data_dir = Path(__file__).parent / 'data' / 'raw'
        output_dir = Path(__file__).parent / 'reports' / 'figures'
        os.makedirs(output_dir, exist_ok=True)

        maquinas = pd.read_csv(data_dir / 'maquinas.csv')
        sensores = pd.read_csv(data_dir / 'sensores.csv')
        medicoes = pd.read_csv(data_dir / 'medicoes.csv')
        print("✅ Dados carregados com sucesso!")
    except FileNotFoundError as e:
        print(f"❌ Erro: Arquivo não encontrado. Execute 'generate_data.py' primeiro.")
        print(e)
        return

    # --- 2. Análise Inicial ---
    print("\n--- Informações Gerais ---")
    print("\n[Máquinas]")
    maquinas.info()
    print("\n[Sensores]")
    sensores.info()
    print("\n[Medições]")
    medicoes.info()

    print("\n--- Estatísticas Descritivas (Medições) ---")
    print(medicoes.describe())

    # --- 3. Visualizações ---
    print("\n📊 Gerando e salvando visualizações...")

    # Histograma de Temperatura
    plt.figure(figsize=(10, 6))
    sns.histplot(data=medicoes, x='temp', bins=30, kde=True)
    plt.title('Distribuição de Temperatura')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Contagem')
    hist_path = output_dir / 'temperatura_distribuicao.png'
    plt.savefig(hist_path)
    plt.close()
    print(f"   -> Gráfico salvo em: {hist_path}")

    # Boxplot de Temperatura por Sensor
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=medicoes, x='cd_sensor', y='temp')
    plt.title('Distribuição de Temperatura por Sensor')
    plt.xlabel('Sensor')
    plt.ylabel('Temperatura (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    boxplot_path = output_dir / 'temperatura_por_sensor_boxplot.png'
    plt.savefig(boxplot_path)
    plt.close()
    print(f"   -> Gráfico salvo em: {boxplot_path}")

    print("\n🎉 Análise Exploratória concluída!")

if __name__ == "__main__":
    run_exploratory_analysis()
