# exercici 1
import pandas as pd
import os

# obtenim el directori actual
script_dir = os.getcwd()

# construïm el file_path del dataset
file_path = os.path.join(script_dir, 'PAC4_PCD', 'data', 'dataset.csv')

# carreguem el fitxer csv en df
df = pd.read_csv(file_path, sep=';')

# Mostrar els 5 primers valors
print(df.head(5))

# Nombre de ciclistes
print(f'Hi ha un total de {len(df['biker'].unique())} ciclistes')

# Total de columnes
print(f'El dataframe conté un total de {df.shape[0]} columnes.')
