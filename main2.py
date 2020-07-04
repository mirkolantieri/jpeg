from models.dctHome import Home
import time
import plotly.express as px
import numpy as np
import csv
import pandas as pd

"""
dimension_array = np.linspace(25, 700, num=28)
time_array_library_dct = []
time_array_my_dct = []
h = Home()

for dimension in dimension_array:
    print("Computazione dimensioni in corso: " + str(dimension))
    matrix = h.createMatrix(N=dimension)

    start_time = time.process_time()
    fastDCT = h.fft2(matrix)
    time_array_library_dct.append(time.perf_counter() - start_time)

    start_time = time.process_time()
    myDCT = h.dct(matrix, dimension)
    time_array_my_dct.append(time.process_time() - start_time)



with open('data/data.csv', 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerows(zip(dimension_array, time_array_library_dct, time_array_my_dct))

"""

df = pd.read_csv ('data/data.csv')

fig = px.line (df, x=df['Dimensione'], y=['FFT'], title='Grafico della trasformata FFT').show()

fig2 = px.line (df, x=df['Dimensione'], y=['DCTHome'], title='Grafico della trasformata DCT Home').show()

fig3 = px.line (df, title='Grafico di confronto delle trasformate DCT').show()
