# preguntes exercici 1
print("Preguntes exercici 1")
import exercici_1 as ex1

# obtenim el df a partir del dataset.csv emmagatzemat a la carpeta data
df = ex1.get_monegros_df ()

# mostrem per pantalla les primeres 5 files
ex1.primers_cinc (df)

# ciclistes que van participar a la prova
ex1.total_ciclistes (df)

# total columnes al df
ex1.total_columnes (df)

# Preguntes exercici 2
import exercici_2 as ex2

# redefinim el df, ara amb els noms generats de forma aleatòria
df = ex2.name_surname (df)

# mostrem el df amb els noms nous
ex1.primers_cinc (df)

# eliminem els ciclistes que es van quedar sense participar
df = ex2.remove_dns (df)

# el total de ciclistes després de correr les funcions anteriors
ex1.total_ciclistes (df)

# tornem a mostrar els 5 primers
ex1.primers_cinc (df)

# les dades del ciclista amb dorsal 1000:
ex2.get_thousandth_cyclist (df)

# Preguntes exercici 3
import exercici_3 as ex3

# creem la nova columna amb els temps simplificats per grups de 20 minuts
df = ex3.time_grouped_column (df)

print("Mostrem els 15 primers resultats")
print(df.head(15))

# creem el df agrupat per franges de 20 minuts
df_grouped_time = ex3.time_grouped_df (df)

# mostrem els 5 primers resultats
ex1.primers_cinc(df_grouped_time)

# generem l'histograma, que es guarda automàticament a la carpeta img
ex3.create_histogram (df_grouped_time)

# Preguntes exercici 4
print("Preguntes exercici 4:")
import exercici_4 as ex4

# netegem la columna club mitjançant la funció clean_club definida al mòdul exercici_4.py
df = ex4.clean_club (df)

print('Mostrem els 15 primers resultats del df amb la columna "club" netejada:')
print(df.head(15))

# Preguntes exercici 5
print("Preguntes exercici 5")
import exercici_5 as ex5

# a partir del df amb la columna club netejada, responem a les preguntes sobre els participants de la UCSC
# llistat de ciclistes del club
ex5.ciclistes_ucsc (df)

# ciclista més ràpid, posició real i percentatge sobre el total
ex5.millor_temps_ucsc (df)