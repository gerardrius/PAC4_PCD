import matplotlib.pyplot as plt
import os

def minutes_002040 (time_instance):
    '''
    Funció que arrodoneix una instància temps per grups de 20 minuts (e.g. '01:02:31' -> '01:00'):

    Args:
        pren una instància de temps com a argument, en format string 'hh:mm:ss'.

    Returns:
        :obj:`str`: retorna la nova instància de temps en format 'hh:mm'
    '''
    # definim les variables hours (que traslladarem directament al valor retornat) i minutes, que emprarem per comprovar a quin grup horari pertany
    hours = time_instance[:5].split(':')[0]
    minutes = int(time_instance[:5].split(':')[1])

    # en funció del valor dels minuts, assignem el valor corresponent
    if minutes < 20:
        minutes = '00'
    elif minutes < 40:
        minutes = '20'
    else:
        minutes = '40'

    # construïm la string resultant
    time = hours + ':' + minutes
    return time

def time_grouped_column (df):
    '''
    Funció que crea una nova columna al df amb les dades de temps agrupades per bins de 20 minuts:

    Args:
        pren el dataframe de referència com a argument.

    Returns:
        :obj:`pandas.DataFrame`: retorna el dataframe amb una nova columna (time_grouped)
    '''
    # creem la nova columna aplicant la funció minutes_002040 mitjançant una lambda
    df['time_grouped'] = df['time'].apply(lambda x: minutes_002040(x))

    print('Simplificació dels temps per franges de 20 minuts realitzada!')

    return df

def time_grouped_df (df):
    '''
    Funció que crea un nou df amb dues columnes, una per cada grup de temps, i l'altra amb el nombre de participants al grup:

    Args:
        pren el dataframe de referència com a argument.

    Returns:
        `pandas.DataFrame`: retorna el dataframe agrupat per time_grouped
    '''
    # filtro el df per quedar-me únicament amb les columnes de time_grouped i dorsals, per fer el recompte de participants per cada franja
    df = df[['time_grouped', 'dorsal']].groupby('time_grouped').count().reset_index()
    
    # reanomeno la columna dorsal per num_participants
    df.rename(columns={'dorsal': 'num_participants'}, inplace=True)

    print("S'ha creat el nou dataframe amb l'agrupació de ciclistes per franja de temps!")

    return df


def create_histogram (grouped_df):
    '''
    Funció que crea i emmagatzema l'histograma resultant de l'agrupació dels temps de finalització dels participants

    Args:
        pren el dataframe agrupat com a argument.

    Returns:
        no retorna cap argument, simplement guarda el document img de l'histograma
    '''
    # creem el gràfic
    plt.bar(grouped_df['time_grouped'], grouped_df['num_participants'], width=0.9, edgecolor='black')

    # afegim el nom de cada eix i el títol de l'histograma
    plt.xlabel('Time group')
    plt.ylabel('# participants')
    plt.title('Time Distribution Histogram')

    # rotem l'eix per evitar que els labels es solapin
    plt.xticks(rotation=45, ha='right')  

    # defineixo el path relatiu al cwd per a emmagatzemar la imatge histograma.png a la carpeta img
    img_folder = os.path.join(os.getcwd(), "img")
    img_path = os.path.join(img_folder, "histograma.png")

    # m'asseguro que la carpeta img existeix
    os.makedirs(img_folder, exist_ok=True)

    # Guardo l'histograma com a fitxer png
    plt.savefig(img_path, format='png', dpi=300)

    print(f"Histograma guardat a: {img_path}")
