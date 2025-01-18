# main file
import os
os.getcwd()

import exercici_1 as ex1
import exercici_2 as ex2
import exercici_3 as ex3

df = ex1.get_monegros_df()
print(df.head())

df = ex2.remove_dns (df)
print('removed dns')

grouped_df = ex3.time_agrupation (df)
print('grouped df by time bins')

ex3.create_histogram (grouped_df)

# print(os.path.join(os.getcwd(), "img"))











