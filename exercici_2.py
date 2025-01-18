# definim les funcions necesàries per a realitzar la neteja del dataset

# Tot i que les dades que et proporcionem ja estan anonimitzades, anem a suposar que són les 
# dades reals, i que les volem anonimitzar. Pots utilitzar la llibreria Faker per generar noms 
# i cognoms (en anglès).

# from exercici_1 import get_monegros_df

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

# Executa la funció, i mostra els 5 primers valors del dataframe. -> al main.py

# Els ciclistes que tenen un temps 00:00:00 significa que no van participar a la prova 
# (estaven inscrits però no van fer la cursa). Elimina'ls del dataset.

def remove_dns (df):
    '''
    Funció que esborra les files en què el valor de time és '00:00:00':

    Args:
        pren el dataframe amb dades de la cursa dels Monegros com a referència.

    Returns:
        :obj:`pandas.DataFrame`: df filtrat per ciclistes que sí que han participat a la cursa
    '''
    # filtrem per la condició que el registre de temps no sigui 00:...
    df = df[df['time'] != '00:00:00']
    return df

# Quants ciclistes tenim ara en el dataframe? Mostra els 5 primers. 
# Per a respondre a aquesta pregunta podem recórrer a la funció definida al mòdul exercici_1.py -> total_ciclistes (df)

# Recupera les dades del ciclista amb dorsal=1000.
def get_thousandth_cyclist (df):
    '''
    Funció que retorna les dades del ciclista amb dorsal 1000.

    Args:
        pren el dataframe amb dades de la cursa dels Monegros com a referència.

    Returns:
        :obj:`pandas.DataFrame`: mostra una única fila amb les dades del ciclista amb dorsal 1000, en cas que hagi participat a la cursa.
    '''
    try:
        print(df[df['dorsal'] == 1000])
    except:
        print('El ciclista amb dorsal 1000 no ha començat la cursa!')

