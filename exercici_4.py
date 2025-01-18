# CLUBS CICILISTES!

# Volem netejar (bastant, sense pretendre fer-ho perfecte)

def club_to_upper (df):
    '''
    Funció que canvia els caràcters de la columna club a majúscules

    Args:
        pren el dataframe de referència com a argument.

    Returns:
        :obj:`pandas.DataFrame`: retorna el dataframe amb la columna club modificada
    '''
    df['club_clean'] = df['club_clean'].apply(lambda x: x.upper())
    return df

def remove_club_type (df):

    valors_a_eliminar = ['PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB ']
    def remover (club_instance):
        for value in valors_a_eliminar:
            club_instance = club_instance.replace(value, '')
        return club_instance

    df['club_clean'] = df['club_clean'].apply(lambda x: remover(x))

    return df

def remove_initials (df):
    '''
    Funció per esborrar les abreviacions especificades a l'inici de la string de la columna club

    Args:
        df (DataFrame): el df de referència amb la columna "club".

    Returns:
        DataFrame: el df modificat sense les abreviacions inicials
    '''

    # definim el patró d'expressions regulars per tal que coincideixin amb les abreviatures especificades
    pattern = r'^(C\.C\. |C\.C |CC |C\.D\. |C\.D |CD |A\.C\. |A\.C |AC |A\.D\. |A\.D |AD |A\.E\. |A\.E |AE |E\.C\. |E\.C |EC |S\.C\. |S\.C |SC |S\.D\. |S\.D |SD )'

    # reemplacem les coincidencies per no res
    df['club_clean'] = df['club_clean'].str.replace(pattern, '', regex=True)

    return df

def remove_last_part (df):
    '''
    Funció per esborrar les abreviacions especificades al final de la string de la columna club

    Args:
        df (DataFrame): el df de referència amb la columna "club".

    Returns:
        DataFrame: el df modificat sense les abreviacions finals
    '''

    # definim el patró d'expressions regulars per tal que coincideixin amb les abreviatures especificades
    pattern = r'( T\.T\.| T\.T| TT| T\.E\.| T\.E| TE| C\.C\.| C\.C| CC| C\.D\.| C\.D| CD| A\.D\.| A\.D| AD| A\.C\.| A\.C| AC)$'

    # reemplacem les coincidencies per no res
    df['club_clean'] = df['club_clean'].str.replace(pattern, '', regex=True)

    return df

# Finalment, elimina possibles espais en blanc al principi o al final de la cadena.
def trim_club_name (df):
    '''
    Funció per esborrar els espais tant a l'inici com al final de la string de club

    Args:
        df (DataFrame): el df de referència amb la columna "club".

    Returns:
        DataFrame: el df modificat sense espais ni a l'inici ni al final
    '''
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

# funció sencera
def clean_club (df):
    '''
    Funció per netejar i els noms de la columna "club".

    Aplica les funcions definides prèviament:
    1. Converteix tots els caràcters a majúscules.
    2. Elimina valors específics definits a "valors_a_eliminar".
    3. Elimina les abreviacions especificades al principi de la string.
    4. Elimina les abreviacions especificades al final de la string.
    5. Elimina possibles espais en blanc al principi o al final de la cadena.

    Args:
        df (DataFrame): el DataFrame de referència amb la columna "club".

    Returns:
        DataFrame: el DataFrame netejat.
    '''
    # primer creem una columna nova, per tal d'incloure-hi el nom del club netejat
    df['club_clean'] = df['club']

    # 1: Convertir a majúscules
    df = club_to_upper(df)

    # 2: Eliminar valors específics
    df = remove_club_type(df)

    # 3: Eliminar abreviacions al principi
    df = remove_initials(df)

    # 4: Eliminar abreviacions al final
    df = remove_last_part(df)

    # 5: Eliminar espais en blanc al principi i al final
    df = trim_club_name(df)

    print("S'ha realitzat la neteja de la columna 'club' correctament!")

    return df

# Crear un df amb agrupació per nom del club, i sort_by num_participants desc
def club_agrupation (df):
    '''
    Funció que crea un nou df agrupant els clubs per nombre participants :

    Args:
        pren el dataframe de referència com a argument.

    Returns:
        `pandas.DataFrame`: retorna un df de dues columnes: club i num_participants
    '''

    # filtro el df per quedar-me únicament amb les columnes de time_grouped i dorsals, per fer el recompte de participants per cada franja
    df = df[['club', 'dorsal']].groupby('club').count().reset_index()
    
    # reanomeno la columna dorsal per num_participants
    df.rename(columns={'dorsal': 'num_participants'}, inplace=True)

    df = df.sort_values(by='num_participants', ascending=False)

    print("S'ha creat un nou dataframe amb l'agrupació de ciclistes per club, ordenat de més a menys membres.")

    return df
    