import pandas as pd
import os

def generate_stats():
    file_path = "data/historico_vacantes.csv"
    if not os.path.exists(file_path):
        print("Aún no hay datos. Corre el engine.py primero.")
        return

    df = pd.read_csv(file_path)
    print("\n--- 📈 RESUMEN DE MERCADO LABORAL ---")
    print(f"Total vacantes registradas: {len(df)}")
    print("\nTop puestos con más oferta:")
    print(df['Puesto'].value_counts())
    print("\nPlataformas más activas:")
    print(df['Plataforma'].value_counts())

if __name__ == "__main__":
    generate_stats()