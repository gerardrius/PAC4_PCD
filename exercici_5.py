# Quins són els ciclistes de la UCSC (Unió Ciclista Sant Cugat)?
# Quin ciclista de la UCSC ha fet millor temps?
# En quina posició sobre el total ha quedat aquest ciclista, i quin percentatge sobre el total representa?

# a partir del df de

def ciclistes_ucsc (df):
    ucsc = df[df['club'] == 'UCSC']

    ucsc_bikers = ucsc['biker'].to_list()

    print(f'Els ciclistes de la UCSC són els següents: {ucsc_bikers}')

def millor_temps_ucsc (df):
    ucsc = df[df['club'] == 'UCSC']

    def temps_en_segons (temps_str):
        hores = int(temps_str.split(':')[0])
        minuts = int(temps_str.split(':')[1])
        segons = int(temps_str.split(':')[2])
        
        temps = hores*3600 + minuts*60 + segons
        return temps

    ucsc['temps_real'] = ucsc['time'].apply(lambda x: temps_en_segons (x))

    ucsc = ucsc.sort_values(by='temps_real', ascending=True)
    ciclista_1 = ucsc.iloc[0]['biker']

    # resposta al nom del ciclista més ràpid del UCSC
    print(f'El ciclista més ràpid del club UCSC ha estat {ciclista_1}.')

    # per trobar la posició, faig reset de l'index (he observat que parteix de 83, possiblement degut als participants que no han près part a la cursa)
    df = df.reset_index()

    posicio_real = df[df['biker'] == ciclista_1].index[0] + 1 # sumem 1 ja que l'index comença per 0
    print(f'El {ciclista_1} ha acabat la prova en la {posicio_real}a posició')

    # pel percentatge, dividim la posició entre el total de participants i multipliquem per 100
    percentatge = round((posicio_real/df.shape[0])*100, 2)
    print(f'En percentatge, això significa estar entre els millors {percentatge}% participants.')