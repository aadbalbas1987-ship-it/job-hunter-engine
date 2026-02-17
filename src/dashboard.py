import pandas as pd
from datetime import datetime, timedelta
import os

def generate_weekly_dashboard():
    file_path = "data/historico_vacantes.csv"
    if not os.path.exists(file_path):
        print("❌ No hay datos acumulados todavía. Corré el engine.py.")
        return

    # Cargamos los datos
    df = pd.read_csv(file_path)
    
    # Convertimos la columna Fecha a formato real de Python
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Filtro: Solo lo publicado en los últimos 7 días
    hace_una_semana = datetime.now() - timedelta(days=7)
    df_fresco = df[df['Fecha'] >= hace_una_semana]

    print(f"\n" + "="*40)
    print(f"📈 DASHBOARD ESTRATÉGICO (ÚLTIMOS 7 DÍAS)")
    print(f"Total vacantes activas: {len(df_fresco)}")
    print("="*40)

    if not df_fresco.empty:
        print("\n🔥 PUESTOS CON MÁS DEMANDA:")
        print(df_fresco['Puesto'].value_counts())
        
        print("\n🌐 PLATAFORMAS MÁS ACTIVAS:")
        print(df_fresco['Plataforma'].value_counts())
    else:
        print("⚠️ No se encontraron vacantes frescas en la base de datos.")
    
    print("="*40 + "\n")

if __name__ == "__main__":
    generate_weekly_dashboard()