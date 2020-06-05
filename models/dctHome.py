"""
FIle dctHome.py : include la prima parte del progetto per la libreria fatta in casa,
da confrontare con la versione fast che viene offerta da fftpack (modulo scipy)
"""


 
import numpy as np
from scipy import fftpack


class Home():
    
    def __ini__(self):
        return

  
    def createMatrix(N):
        return np.asarray(np.random.randint(0, 255, (N,N)))
    
    
    def DCT2(matrix, N):
        dct = np.array(matrix)
        if N < 0:
           N = np.abs(N)
       
        for i in np.arange(matrix.size):
            for j in np.arange(matrix.size):
                    dct[:N, :N] = fftpack.fft(fftpack.fft( matrix[:N,:N], axis=0), axis=1 )
        
            
        print("DCT2 Libreria Fast:")
        print()
        print(np.array(dct))
        return dct

    
    def customDCT(matrix, f):
        dct = np.array(matrix)
        if f < 0:
           f = np.abs(f)
       
        for i in np.arange(matrix.size):
            for j in np.arange(matrix.size):
                dct[i:i+f, j:j+f] = ( dct[i:i+f, j:j+f] * np.cos(np.pi*i*(2*i-1)/(2*f)) * np.cos(np.pi*j*(2*j-1)/(2*f)))
                    
        print("DCT2 Libreria Custom:")
        print()
        print(np.array(dct))
        return dct