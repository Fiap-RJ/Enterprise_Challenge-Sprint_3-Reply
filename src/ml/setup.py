import os
import sys
from pathlib import Path

def create_directories():
    """Cria a estrutura de diretórios necessária"""
    base_dirs = [
        'data/raw',
        'data/processed',
        'models',
        'notebooks',
        'src',
        'utils'
    ]
    
    for dir_name in base_dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Diretório criado: {dir_name}")
    
    # Criar arquivos .gitkeep nos diretórios vazios
    for root, dirs, _ in os.walk('.'):
        for dir_name in dirs:
            gitkeep_path = os.path.join(root, dir_name, '.gitkeep')
            if not os.path.exists(gitkeep_path):
                with open(gitkeep_path, 'w') as f:
                    pass
                print(f"Arquivo .gitkeep criado em: {gitkeep_path}")

def install_requirements():
    """Instala as dependências do projeto"""
    requirements_path = os.path.join('..', '..', '..', 'requirements.txt')
    if os.path.exists(requirements_path):
        print("\nInstalando dependências...")
        os.system(f"pip install -r {requirements_path}")
    else:
        print(f"\n⚠️ Arquivo {requirements_path} não encontrado!")
        print("Certifique-se de que você está executando este script do diretório src/ml")

def setup_jupyter_kernel():
    """Configura o kernel do Jupyter"""
    print("\nConfigurando kernel do Jupyter...")
    os.system("python -m ipykernel install --user --name=venv --display-name=\"Python (venv)\"")

def main():
    print("🚀 Configurando o ambiente do projeto...")
    
    # Criar estrutura de diretórios
    create_directories()
    
    # Instalar dependências
    install_requirements()
    
    # Configurar Jupyter
    setup_jupyter_kernel()
    
    print("\n✅ Configuração concluída com sucesso!")
    print("\nPróximos passos:")
    print("1. Ative o ambiente virtual:")
    print("   - Windows: .venv\\Scripts\\activate")
    print("   - Linux/Mac: source .venv/bin/activate")
    print("\n2. Execute o notebook de geração de dados:")
    print("   jupyter notebook notebooks/01_data_generation.ipynb")

if __name__ == "__main__":
    main()
