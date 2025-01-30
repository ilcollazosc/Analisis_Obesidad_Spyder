import pandas as pd
datos=pd.read_csv('ObesityDataSet.csv')
peso_promedio=datos.groupby('Gender')['Weight'].mean()
print(peso_promedio)