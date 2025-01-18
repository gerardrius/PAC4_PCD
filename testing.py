# farem un test per la funció clean_club, que és la més extensa.
import pandas as pd

import exercici_1 as ex1
import exercici_2 as ex2
import exercici_4 as ex4

# defineixo el df per tal de testejar-lo
df = ex1.get_monegros_df ()

# únicament aplico la funció per eliminar les columnes dels no participants i crear la columna neta de club 
# (la resta de funcions per agrupar els temps per franges de 20', per exemple, no fan falta)
df = ex2.remove_dns (df)

df = ex4.clean_club (df)
