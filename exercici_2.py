# definim les funcions necesàries per a realitzar la neteja del dataset

# Tot i que les dades que et proporcionem ja estan anonimitzades, anem a suposar que són les 
# dades reals, i que les volem anonimitzar. Pots utilitzar la llibreria Faker per generar noms 
# i cognoms (en anglès).

# from exercici_1 import get_monegros_df
import exercici_1 as ex1

df = ex1.get_monegros_df()


# Defineix la funció name_surname(df), que li passarem com a argument el dataframe, i ens 
# retornarà el nou dataframe amb els noms canviats (columna biker).
from faker import Faker

def name_surname (df):
    '''
    Anonimitza la columna biker:

    Args:
        pren el dataframe amb dades de la cursa dels Monegros com a referència.

    Returns:
        :obj:`pandas.DataFrame`: 
    '''
    # creem una instància de Faker()
    fake = Faker()

    # Canviem els noms de cada fila dins la columna biker per noms aleatoris
    df['biker'] = df.apply(lambda x: fake.name(), axis=1)

    return df

name_surname (df).head(5)

# Executa la funció, i mostra els 5 primers valors del dataframe.

# Els ciclistes que tenen un temps 00:00:00 significa que no van participar a la prova 
# (estaven inscrits però no van fer la cursa). Elimina'ls del dataset.

# Quants ciclistes tenim ara en el dataframe? Mostra els 5 primers. Recupera les dades del 
# ciclista amb dorsal=1000.