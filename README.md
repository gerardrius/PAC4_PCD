# PAC4_PCD

En primer lloc, he creat un repositori a github per inicialitzar el projecte
He clonat el repositori directament al meu local emprant el link
Dins la carpeta PAC4 he inclòs la carpeta “data”, que conté el csv amb els resultats de la cursa ciclista Monegros.

He creat un virtual environment, en el què he instal·lat les llibraries necessàries per al projecte (pandas, numpy, etc.)

Seguidament, he creat els fitxers necessaris per al projecte dins la pròpia carpeta PAC4 (main.py, exercici_1.py, etc.)

Al file exercici_1.py hi he definit les funcions necessàries per obtenir el dataframe a partir del csv que tenim a la carpeta data. També hi he creat les diverses funcions que ens permeten mostrar la informació del df que es demana a l'exercici 1; les 5 primeres files, el nombre de participants i la longitud del df.

Al file exercici_2.py hi he creat les funcions per anonimitzar els noms dels ciclistes, per filtrar el df per quedar-nos únicament amb les dades d'aquells ciclistes que han participat a la cursa, i per últim, per mostrar les dades del ciclista amb dorsal 1000.

Per l'exercici_3.py, en primer lloc he creat una funció que modifica els valors de la columna time per tal d'agrupar la columna per bins de 20 minuts.