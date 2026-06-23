import pandas as pd

def ejecutar_macro_analisis():

    try:
        df_fraud = pd.read_csv('datos_crudos/fraud_oracle.csv')
        df_motor_1 = pd.read_csv('datos_crudos/motor_data11-14lats.csv')
        df_motor_2 = pd.read_csv('datos_crudos/motor_data14-2018.csv')
        return df_fraud, df_motor_1, df_motor_2
    except FileNotFoundError:
        print("Error: No se encontraron los archivos. ")
        return
    
def informacion(df):
    dimensiones = f"Las dimensiones del dataframe es de:\n {df.shape}"
    # datos = f"Los tipos de datos del dataframe son:\n {df.dtypes}"

    print(dimensiones)
    print("*"*40)
    print(f"Resumen del datafram es:\n {df.info()}")
    print("--"*40)
    print(f"Primeros 3 datos:\n {df.head(3)}")
    print("--"*40)
    print(f"Primeros 3 datos completos:\n {df.head(3).T}")

def info_comp(df):
    print(f"Informacion estadistica inicial:\n")
    print(df.describe())
    print('--'*60)

    print(f"total de datos nulos:")
    print(df.isnull().sum())
    print('--'*60)

    print(f"Datos duplicados:")
    print(df.duplicated().sum())
    print('--'*60)

    print(f"Estadistica descriptiva de texto")
    print(df.describe(include=str).T)

if __name__ == '__main__':
    df_fraud, df_motor_1, df_motor_2 = ejecutar_macro_analisis()
    print("Primeros datos del dataframe llamado 'df_motor_1':")
    # info_comp(df_fraud)
    informacion(df_motor_1)
