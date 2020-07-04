"""
FIle dctHome.py : include la prima parte del progetto per la libreria fatta in casa,
da confrontare con la versione fast che viene offerta da fftpack (modulo scipy)
"""

import numpy as np
from scipy import fftpack


class Home:
    def createMatrix(self, N):
        return np.random.randint(0, 255, (int(N), int(N)))

    def fft2(self, matrix):
        dct = fftpack.fft(fftpack.fft(matrix, axis=0), axis=1)
        return dct

    def dct(self, matrix, N):
        dct = np.copy(matrix)
        Nx = matrix.shape[0]
        Ny = matrix.shape[1]

        if N < 0:
            N = np.abs(N)

        for i in range(Ny):
            col = dct[:, i]
            dct_col = Home.dctMono(col)
            dct[:, i] = dct_col

        for i in range(Nx):
            row = dct[:, i]
            dct_row = Home.dctMono(row)
            dct[i, :] = dct_row

        return dct

    def dctMono(f):
        n = f.size
        a = np.zeros(n)
        dct = np.zeros(n)

        a[0] = 1 / np.sqrt(n)
        a[1:] = 2 / np.sqrt(n)

        for k in range(n):
            for i in range(n):
                dct[k] += f[i] + np.cos(np.pi * k * (2 * i - 1) / (2 * n))
            dct[k] = a[k] * dct[k]

        return dct
