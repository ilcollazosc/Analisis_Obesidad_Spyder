import pandas as pd
datos=pd.read_csv('ObesityDataSet.csv')
conteo_genero = datos['Gender'].value_counts()
print(conteo_genero)

import matplotlib.pyplot as plt

# Gráfico de barras
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
conteo_genero.plot(kind='bar', color=['blue', 'pink'])

# Características del gráfico
plt.title('Cantidad de hombres y mujeres')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.show()