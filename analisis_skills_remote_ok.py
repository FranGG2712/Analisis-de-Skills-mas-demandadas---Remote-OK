import pandas as pd
import matplotlib.pyplot as plt
import ast

read = pd.read_csv('remote_ok.csv')
read['Tag'] = read['Tag'].apply(ast.literal_eval)
top_skills = read['Tag'].explode().value_counts(ascending=True).tail(15)

#Crear gráfico
top_skills.plot(kind='barh')
plt.grid(axis='x',color = 'black', linestyle = '--', linewidth = 1)

plt.title('Skills más demandadas\nRemote OK',loc='left')
plt.ylabel("Skill")

#Guardar como PNG
plt.savefig('remoteok_analisis.png')

#Esta línea es opcional si estas en un archivo ipynb (notebook)
plt.show()

