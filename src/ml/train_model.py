import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

def train_model():
    """Carrega os dados, treina um modelo de regressão e o salva."""
    print("🚀 Iniciando o treinamento do modelo...")

    # --- 1. Carregamento dos Dados ---
    try:
        # Definir diretórios
        base_dir = Path(__file__).parent
        data_dir = base_dir / 'data' / 'raw'
        model_dir = base_dir / 'models'
        reports_dir = base_dir / 'reports' / 'figures'
        os.makedirs(model_dir, exist_ok=True)
        os.makedirs(reports_dir, exist_ok=True)

        medicoes = pd.read_csv(data_dir / 'medicoes.csv')
        sensores = pd.read_csv(data_dir / 'sensores.csv')
        print("✅ Dados carregados com sucesso!")
    except FileNotFoundError as e:
        print(f"❌ Erro: Arquivo não encontrado. Execute 'generate_data.py' primeiro.")
        print(e)
        return

    # --- 2. Pré-processamento e Feature Engineering ---
    print("\n⚙️  Pré-processando os dados...")
    # Juntar medições com informações dos sensores
    df = pd.merge(medicoes, sensores, on='cd_sensor')

    # Converter colunas categóricas em numéricas (One-Hot Encoding)
    df = pd.get_dummies(df, columns=['cd_sensor', 'tipo', 'modelo'], drop_first=True)

    # Remover colunas que não serão usadas no modelo
    df = df.drop(columns=['cd_medicao', 'data', 'cd_maq', 'inicio_operacao', 'termino_opercao'])

    # Definir features (X) e alvo (y)
    X = df.drop('temp', axis=1)
    y = df['temp']

    # --- 3. Divisão dos Dados ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"   -> Dados divididos: {len(X_train)} para treino, {len(X_test)} para teste.")

    # --- 4. Treinamento do Modelo ---
    print("\n🧠 Treinando o modelo RandomForestRegressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    # --- 5. Avaliação do Modelo ---
    print("\n📈 Avaliando o modelo...")
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"   -> Mean Squared Error (MSE): {mse:.4f}")
    print(f"   -> R² Score: {r2:.4f}")

    # --- 6. Gerar Gráfico de Performance ---
    print("\n📊 Gerando gráfico de performance do modelo...")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6, s=80)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2, label='Previsão Perfeita')
    plt.title('Performance do Modelo: Valores Reais vs. Previstos', fontsize=16)
    plt.xlabel('Temperatura Real (°C)', fontsize=12)
    plt.ylabel('Temperatura Prevista (°C)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    performance_plot_path = reports_dir / 'modelo_performance.png'
    plt.savefig(performance_plot_path)
    plt.close()
    print(f"   -> Gráfico de performance salvo em: {performance_plot_path}")

    # --- 7. Salvando o Modelo ---
    model_path = model_dir / 'temperature_prediction_model.joblib'
    joblib.dump(model, model_path)
    print(f"\n💾 Modelo salvo em: {model_path}")

    print("\n🎉 Processo de treinamento concluído!")

if __name__ == "__main__":
    train_model()
