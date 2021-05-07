""" Il file main.py contiene una semplice interfaccia per l'utente in cui si
ha la possibilità  di scegliere le immagini attuali del programma oppure
con altre immagini caricate sul folder

"""

# importo delle librerie necessarie


from models.jpeg import *
from sys import exit
import time
import imageio as imread

print("\t\t ^^^^^^^^^ Programma JPEG ^^^^^^^^^ \n\n")
print("1. Inizia programma\n0. Esci dal programma\n\n")

g = input("Selezionare scelta:\t")

if g == "0":
    exit(1)

if g != "0":
    print("\nImmagini disponibili:" + "\n1.BabyYoda.bmp"
          + "\n2.C3PO.bmp"
          + "\n3.DarthVader_DeathStar.bmp"
          + "\n4.DarthVader.bmp" + "\n5.MilleniumFalcon.bmp\n\n")

    scelta = input("Scegliere tra le immagini disponibili:\t")

    if scelta == "1":
        image = 'data/BabyYoda.bmp'
    elif scelta == "2":
        image = 'data/C3PO.bmp'
    elif scelta == "3":
        image = 'data/DarthVader_DeathStar.bmp'
    elif scelta == "4":
        image = 'data/DarthVader.bmp'
    else:
        image = 'data/MilleniumFalcon.bmp'

    start = time.perf_counter()


    f = input("Scegliere la dimensione del blocco F:\t")

    d = input("Scegliere il taglio d tra [0: 2F-2]:\t")

    display_images(image, f, d)

    end = time.perf_counter()

    print(end - start, "Tempo di esecuzione")
    print()
