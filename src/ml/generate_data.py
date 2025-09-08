import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from pathlib import Path

def setup_directories():
    """Garante que os diretórios necessários existam"""
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)

def generate_machines(n=5):
    """Gera dados sintéticos para a tabela T_MAQUINA"""
    tipos = ['Fresadora', 'Torno CNC', 'Retífica', 'Furadeira', 'Plasma']
    modelos = ['Modelo A', 'Modelo B', 'Modelo C', 'Modelo D', 'Modelo E']
    
    data = []
    for i in range(1, n+1):
        data.append({
            'cd_maq': f'M{str(i).zfill(4)}',
            'tipo': random.choice(tipos),
            'modelo': random.choice(modelos),
            'ano': random.randint(2018, 2023),
            'inicio_opercao': (datetime.now() - timedelta(days=random.randint(30, 1000))).strftime('%Y-%m-%d'),
            'termino_operacao': None
        })
    
    return pd.DataFrame(data)

def generate_sensors(machines_df, n_sensors=10):
    """Gera dados sintéticos para a tabela T_SENSOR"""
    tipos_sensor = ['Temperatura', 'Vibração', 'Pressão', 'Corrente', 'Tensão']
    modelos_sensor = ['S-100', 'S-200', 'S-300', 'S-400', 'S-500']
    
    data = []
    sensor_id = 1
    
    for _, machine in machines_df.iterrows():
        for _ in range(random.randint(2, 3)):  # 2-3 sensores por máquina
            install_date = datetime.strptime(machine['inicio_opercao'], '%Y-%m-%d') + timedelta(days=random.randint(0, 30))
            data.append({
                'cd_sensor': f'S{str(sensor_id).zfill(5)}',
                'cd_maq': machine['cd_maq'],
                'tipo': random.choice(tipos_sensor),
                'modelo': random.choice(modelos_sensor),
                'ano': random.randint(2019, 2023),
                'inicio_operacao': install_date.strftime('%Y-%m-%d'),
                'termino_opercao': None
            })
            sensor_id += 1
    
    return pd.DataFrame(data)

def generate_measurements(sensors_df, n_readings=1000):
    """Gera dados sintéticos para a tabela T_MEDICAO"""
    data = []
    
    for _, sensor in sensors_df.iterrows():
        base_temp = random.uniform(20, 30)
        base_humidity = random.uniform(0.4, 0.7)
        
        for _ in range(n_readings // len(sensors_df)):
            timestamp = datetime.now() - timedelta(minutes=random.randint(1, 60*24*30))
            
            # Variação sazonal (dia/noite)
            hour = timestamp.hour
            if 6 <= hour < 18:  # Dia
                temp_variation = random.uniform(-2, 5)
            else:  # Noite
                temp_variation = random.uniform(-5, 2)
                
            temp = base_temp + temp_variation + random.uniform(-1, 1)
            umid = max(0, min(1, base_humidity + random.uniform(-0.1, 0.1)))
            
            data.append({
                'cd_medicao': f'MED{len(data)+1:06d}',
                'cd_sensor': sensor['cd_sensor'],
                'data': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'temp': round(temp, 2),
                'umid': round(umid, 3)
            })
    
    return pd.DataFrame(data)

def main():
    print("🚀 Iniciando geração de dados sintéticos...")
    
    # Configurar diretórios
    setup_directories()
    
    # 1. Gerar dados de máquinas
    print("🔧 Gerando dados de máquinas...")
    machines = generate_machines(5)
    machines.to_csv('data/raw/maquinas.csv', index=False)
    
    # 2. Gerar dados de sensores
    print("📡 Gerando dados de sensores...")
    sensors = generate_sensors(machines, 10)
    sensors.to_csv('data/raw/sensores.csv', index=False)
    
    # 3. Gerar medições
    print("📊 Gerando medições de sensores...")
    measurements = generate_measurements(sensors, 1000)
    measurements.to_csv('data/raw/medicoes.csv', index=False)
    
    # Resumo
    print("\n✅ Dados gerados com sucesso!")
    print(f"- Máquinas: {len(machines)}")
    print(f"- Sensores: {len(sensors)}")
    print(f"- Medições: {len(measurements)}")
    print("\nArquivos salvos em data/raw/")

if __name__ == "__main__":
    main()
