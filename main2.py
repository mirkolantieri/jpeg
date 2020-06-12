from models.home import Home as h
import time
import plotly.express as px
import numpy as np
import csv
import pandas as pd

dimension_array = np.linspace(25, 700, num=28)
time_array_library_dct = []
time_array_my_dct = []
for dimension in dimension_array:
    print("Computazione delle dimensioni: " + str(dimension))
    matrix = h.createMatrix(dimension)

    start_time = time.time()
    fastDCT = h.DCT2(matrix)
    time_array_library_dct.append(time.time() - start_time)

    start_time = time.time()
    myDCT = h.customDCT(matrix, dimension)
    time_array_my_dct.append(time.time() - start_time)

# qui scriviamo il risultato in file csv che ci servirà per registrare i dati
# per poi plottare il grafico
with open('data/data.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerows(zip(dimension_array, time_array_library_dct, time_array_my_dct))


"""
Il codice sotto ci permette di vedere graficamente il comportamento computazionale delle nostre
trasformate


df = pd.read_csv('data/data.csv') # legge il file csv

fig = px.line(df, title='Complessità computazionale delle DCT (Fast e Custom inclusa)')
fig.show()
"""
