import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ejecutar_macro_analisis():
    print("1. Cargando los datasets maestros...")
    try:
        df_fraud = pd.read_csv('master_fraud_data.csv')
        df_motor = pd.read_csv('master_motor_data.csv')
    except FileNotFoundError:
        print("Error: No se encontraron los archivos. Asegúrate de tener 'master_fraud_data.csv' y 'master_motor_data.csv' en la misma ruta.")
        return

    print("2. Estandarizando dimensiones en común...")

    df_fraud['Make_Normalizado'] = df_fraud['Make'].astype(str).str.upper().str.strip()
    df_motor['Make_Normalizado'] = df_motor['MAKE'].astype(str).str.upper().str.strip()

    print("3. Calculando tendencias del dataset de Fraude...")
    # Nombre_De_Tu_Nueva_Columna = ('Columna_Original', 'Operacion_A_Realizar')

    tendencia_fraud = df_fraud.groupby('Make_Normalizado').agg(
        Tasa_Fraude_Porcentaje=('FraudFound_P', lambda x: x.mean() * 100),
        Total_Polizas_Fraude=('PolicyNumber', 'count')
    ).reset_index()

    print("4. Calculando tendencias del dataset de Motor (Logística)...")
    tendencia_motor = df_motor.groupby('Make_Normalizado').agg(
        Promedio_Reclamo_Pagado=('CLAIM_PAID', 'mean'),
        Promedio_Prima_Cobrada=('PREMIUM', 'mean'),
        Total_Polizas_Motor=('OBJECT_ID', 'count')
    ).reset_index()

    print("5. Cruzando los universos (Inner Join por Macro-Tendencias)...")

    macro_analisis = pd.merge(tendencia_fraud, tendencia_motor, on='Make_Normalizado', how='inner')

    macro_analisis = macro_analisis[macro_analisis['Total_Polizas_Fraude'] > 30]

    macro_analisis = macro_analisis.sort_values(by='Tasa_Fraude_Porcentaje', ascending=False)

    macro_analisis.to_csv('resultados_macro_tendencias.csv', index=False)
    print("¡Archivo 'resultados_macro_tendencias.csv' creado con éxito!")

    print("\n7. Generando visualización de los datos...")
    generar_graficas(macro_analisis)

def generar_graficas(df):

    sns.set_theme(style='whitegrid')

    fig,axes = plt.subplots(1,2,figsize=(16,6))

    sns.barplot(
        data=df.head(10),
        x='Tasa_Fraude_Porcentaje',
        y='Make_Normalizado',
        ax = axes[0],
        palette='Reds_r'
    )

    axes[0].set_title('Top 10: Tasa de Fraude por Marca (%)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Tasa de Fraude (%)')
    axes[0].set_ylabel('Marca del Vehículo')

    sns.barplot(
        data=df.head(10), 
        x='Promedio_Reclamo_Pagado', 
        y='Make_Normalizado', 
        ax=axes[1],
        palette='Blues_r'
    )
    axes[1].set_title('Costo Promedio del Reclamo para estas Marcas ($)', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Promedio Pagado por Reclamo')
    axes[1].set_ylabel('')

    plt.show()

if __name__ == '__main__':
    ejecutar_macro_analisis()



