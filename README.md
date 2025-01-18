# PAC4_PCD

En primer lloc, he creat un repositori a github per inicialitzar el projecte
He clonat el repositori directament al meu local emprant el link corresponent.
Dins la carpeta PAC4 he inclòs la carpeta “data”, que conté el csv amb els resultats de la cursa ciclista Monegros.

He creat un virtual environment, en el què he instal·lat les llibraries necessàries per al projecte (pandas, numpy, os, matplotlib etc.)

Seguidament, he creat els fitxers necessaris per al projecte dins la pròpia carpeta PAC4 (main.py, exercici_1.py, etc.)

Exercici 1.
    He definit les funcions necessàries per obtenir el dataframe a partir del csv que tenim a la carpeta data. També hi he creat les diverses funcions que ens permeten mostrar la informació del df que es demana a l'exercici 1; les 5 primeres files, el nombre de participants i la longitud del df.

Exercici 2. 
    He creat les funcions per anonimitzar els noms dels ciclistes, per filtrar el df per quedar-nos únicament amb les dades d'aquells ciclistes que han participat a la cursa, i per últim, per mostrar les dades del ciclista amb dorsal 1000.

Exercici 3.
    En primer lloc he creat una funció que modifica els valors de la columna time per tal d'agrupar la columna per bins de 20 minuts. Seguidament, he creat la funció necessària per a agrupar els participants per franges de temps. En la mateixa funció he filtrat el df quedant-me únicament amb les columnes de franja de temps i dorsal, i he canviat el nom d'aquesta última per 'num_participants', que és més coherent. Per últim, he definit la funció que permet obtenir l'histograma del df agrupat. La imatge resultant es guarda a la carpeta img, dins del repositori PAC4_PCD.

Exercici 4.
    Per l'exercici 4 hem creat un seguit de funcions que ens permeten netejar la columna "club" amb els requeriments que s'especifiquen a l'enunciat (nom en majúscules, sense un seguit de valors especifics ni patrons a l'inici i final de la string, entre d'altres).
    Amb la columna neta, hem creat un subdataframe de dues columnes (club i dorsal) per agrupar el nombre de participants per cada club, ordenant-lo de més a menys participants per club.

Exercici 5.
    En aquest exercici hem creat un parell de funcions per respondre a les preguntes plantejades. La primera filtra el df amb la columna club netejada per quedar-nos únicament amb les files corresponents a ciclistes de la Unió Ciclista Sant Cugat. Es mostra per pantalla la llista de ciclistes del club. A la segona funció es responen la resta de preguntes: ciclista més ràpid, posició real, i percentatge respecte el total de participants.

Un cop acabats tots els mòduls, he definit el guió del main.py, que crida les funcions en l'ordre requerit per l'enunciat de l'activitat per tal de mostrar per pantalla els resultats que es demanen.

També he afegit el document de requeriments mitjançant la corresponent ordre al terminal.
