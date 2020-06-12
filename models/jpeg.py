""" file libreria jpeg per la trasformata di DCT2
"""

#importo delle librerie necessarie

#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from imageio import imread
from scipy import fftpack
import time


class Jpeg:

    # Costruttore: inizializza l'oggetto
    def __init__(self):
        return

################################################################################################

    # definisco una routine per plottare una immagine sola
    def display(image):
        im = imread(image)

        # visualizzo immagine a toni di grigio, tra 0 (nero) to 1 (bianco)

        plt.title("Immagine originale")
        plt.imshow( im, cmap="gray", vmin=0, vmax=1)
        plt.show()

################################################################################################

    # definisco il metodo che ci fornisce la DCT2 e la IDCT2  dell'immagine in cui operiamo

    def DCT2(f):
        return fftpack.dct(fftpack.dct( f, axis=0, norm='ortho' ), axis=1, norm='ortho' )

    def IDCT2(f):
        return fftpack.idct(fftpack.idct( f, axis=0 , norm='ortho'), axis=1 , norm='ortho')

################################################################################################

    # definisco il metodo che ci permette di tagliare la nostra immagine per una certa dimensione

    def cutImage(image, dimension):

        # la condizione if ci serve per risolvere nel caso l'utente inserica un numero negativo
        # per le dimensioni necessarie
        if dimension < 0:
            dimension = np.abs(dimension)

        im = imread(image)

        plt.title("Immagine originale ridimensionata per la dimensione")
        plt.imshow(im[0:dimension,dimension:dimension+dimension], cmap="gray", vmin=0, vmax=1)


################################################################################################

          # definisco il metodo della compressione del blocco con la dct2 "fatta in casa" (dctEncode)

    def dctEncode(image, dim, f,  d):

        start = time.perf_counter()
        if f >= 0:
            im = imread(image)
# --------------------------------------------------------------------------------------
            if d == 0:
                imsize = im.shape
                dct = np.zeros(imsize)


                for i in np.r_[imsize[0]:f]:
                    for j in np.r_[imsize[1]:f]:
                        dct[i:(i+f), j:(j+f)] = np.cos(np.pi*i*(2*i-1)/(2*f)) * np.cos(np.pi*j*(2*j-1)/(2*f))
                        #dct[i:(i+f), j:(j+f)] = Jpeg.DCT2(f) # --- il metodo della libreria già disponibile

                # stampo la matrice del dct
                print(dct)
                plt.show()
                plt.title("Immagine DCT2 dal macro blocco "+ str(f) + "x" +str(f))
                # prendiamo l'espansione uguale a 0.01
                plt.imshow(dct[dim:dim+f,dim:dim+f], cmap="gray", vmax=np.max(dct)*0.01, vmin=0, extent=[0,np.pi,np.pi,0])

# -------------------------------------------------------------------------------------
            elif d == (2*f-2):
                imsize = im.shape
                dct = np.asarray(im)

                for i in np.r_[imsize[0]:f]:
                    for j in np.r_[imsize[1]:f]:
                        if i == f and j == f:
                            dct[i:(i+f), j:(j+f)] = 0
                        dct[i:(i+f), j:(j+f)] = np.cos(np.pi*i*(2*i-1)/(2*f)) * np.cos(np.pi*j*(2*j-1)/(2*f))
                        #dct[i:(i+f), j:(j+f)] = Jpeg.DCT2(f)   # --- il metodo della libreria già disponibile

                # stampo la matrice del dct
                print(dct)
                plt.show()
                plt.title("Immagine DCT2 dal macro blocco "+ str(f) + "x" +str(f))
                plt.imshow(dct[dim:dim+f,dim:dim+f], cmap="gray", vmax=np.max(dct)*0.01, vmin=0, extent=[0,np.pi,np.pi,0])

# --------------------------------------------------------------------------------------
            elif d > 0 and  d < (2*f-2):
                imsize = im.shape
                dct = np.array(im) # converte la dct immagine in array matrice

                for i in np.r_[imsize[0]:f]:
                    for j in np.r_[imsize[1]:f]:
                        while i >= d and j >= d:
                            dct[i:(i+f), j:(j+f)] = 0
                        dct[i:(i+f), j:(j+f)] = np.cos(np.pi*i*(2*i-1)/(2*f)) * np.cos(np.pi*j*(2*j-1)/(2*f))
                    #dct[i:(i+f), j:(j+f)] = Jpeg.DCT2(f) # --- il metodo della libreria già disponibile

                # stampo la matrice del dct
                print(dct)
                plt.show()
                plt.title("Immagine DCT2 dal macro blocco "+ str(f) + "x" +str(f))

                # normalizziamo i valori con 0.01
                plt.imshow(dct[dim:dim+f,dim:dim+f], cmap="gray", vmax=np.max(dct)*0.01, vmin=0, extent=[0,np.pi,np.pi,0])

            end = time.perf_counter()

            print()
            print("Tempo esecuzione DCT2 ", end-start)


        else:
            f = np.abs(f)

################################################################################################

# definisco il metodo della decompressione del blocco con la idct2 "fatta in casa" (idctDecode)

    def idctDecode(image, dim, f,  d):

        if f > 0:
            im = imread(image)
            imsize = im.shape

            # Applico la compressione prima dell'immagine

            Jpeg.dctEncode(image, dim, f, d)

            im_dct = np.asarray(im) # inizializzo la im_dct con la sua correspondente matrice


            # dopo aver letto la matrice e reso la compressione applico la idct

            for i in np.r_[imsize[0]:f]:
                    for j in np.r_[imsize[1]:f]:
                        im_dct[i:(i+f), j:(j+f)] = Jpeg.IDCT2(f)

            # stampo la matrice del idct
            print(im_dct)
            plt.title("Immagine IDCT2 dal blocco "+ str(f) + "x" +str(f))

            # buttiamo i valori al di fuori [0;255] nei parametri vmax e vmin
            plt.imshow(im_dct[dim:dim+f,dim:dim+f], cmap="gray", vmax=255, vmin=0)
            plt.show()

        else:
            f = np.abs(f)

################################################################################################

    # definisco il metodo che mi permette di confrontare l'immagine originale
    # con la sua inversa dct;
    # per facilità il blocco è stato considerato ad una costante 8x8 (64bit)

    def compare(image):
        im = imread(image)
        imsize = im.shape
        im_dct = np.asarray(im)

        for i in np.r_[:imsize[0]:8]:
            for j in np.r_[:imsize[1]:8]:
                im_dct[i:(i+8),j:(j+8)] = Jpeg.IDCT2( Jpeg.DCT2(im_dct[i:(i+8),j:(j+8)] ))

        print(im_dct)


        plt.title("Immagine dopo la compressione DCT2" )
        plt.imshow(im_dct, cmap='gray')
        plt.show()

        """ Questa parte del codice mette in confronto l'immagine originale con quella dopo la compressione
        plt.title("Confronto tra l'immagine originale e quella compressa dal DCT2" )
        plt.imshow(np.hstack((im, im_dct)), cmap='gray')
        plt.show()
        """