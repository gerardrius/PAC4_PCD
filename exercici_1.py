# exercici 1
import pandas as pd
import os



def get_monegros_df ():
    '''
    Defineix un dataframe prenent com a referència les dades del dataset.csv:

    Args:
        no necessita cap argument.

    Returns:
        :obj:`bool`:
    '''
    # obtenim el directori actual
    script_dir = os.getcwd()

    # construïm el file_path del dataset
    file_path = os.path.join(script_dir, 'data', 'dataset.csv')
    
    # carreguem el fitxer csv en df
    df = pd.read_csv(file_path, sep=';')

    return df

def primers_cinc (df):
    '''
    Mostra les 5 primeres files del df:

    Args:
        Necessita un df com a argument.

    Returns:
        No retorna cap valor
    '''
    print(df.head(5))

def total_ciclistes (df):
    '''
    Mostra una el nombre de ciclistes únics que han participat a la cursa:

    Args:
        Necessita un df com a argument.

    Returns:
        No retorna cap valor
    '''
    print(f'Hi ha un total de {len(df['biker'].unique())} ciclistes')

def total_columnes (df):
    '''
    Mostra el total de columnes que té el df que es passa com a argument:

    Args:
        Necessita un df com a argument.

    Returns:
        No retorna cap valor
    '''
    print(f'El dataframe conté un total de {df.shape[0]} columnes.')