import pandas as pd
import numpy as np
import io

def pandas_seguros():

    csv_sucio = """ID_Poliza,Edad_Asegurado,Vehiculo,Monto_Reclamo,Estado_Reclamo
    POL-001,35,VW Jetta,15000.50,Aprobado
    POL-002,,Chevrolet Spark,,Pendiente
    POL-003,19,VW Jetta,8500.00,Rechazado
    POL-004,42,Camioneta,45000.00,Aprobado
    POL-005,999,Chevrolet Spark,12000.00,Aprobado
    POL-006,28,Camioneta,,Rechazado
    """

    df_siniestros = pd.read_csv(io.StringIO(csv_sucio))
    # print(type(df_siniestros))
    # print("Visualizar DataFrame de datos sucios:")
    # print(df_siniestros)

    # df_siniestros.info()
    print(df_siniestros['ID_Poliza'][0])
    jeta = df_siniestros[df_siniestros['Vehiculo'] == 'VW Jetta']
    print(jeta)
    jeta_siniestro = df_siniestros.loc[df_siniestros['Vehiculo'] == 'VW Jetta']
    print(jeta_siniestro)
    

    df_limpio = df_siniestros.dropna(subset=['Monto_Reclamo']).copy()

    df_limpio.loc[df_limpio['Edad_Asegurado'] > 100, 'Edad_Asegurado'] = np.nan

    edad_promedio = df_limpio['Edad_Asegurado'].mean()

    df_limpio['Edad_Asegurado']=df_limpio['Edad_Asegurado'].fillna(edad_promedio)

    print(df_limpio)



if __name__ == '__main__':
    pandas_seguros()
