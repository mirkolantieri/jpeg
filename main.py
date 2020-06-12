""" Il file main.py e ci aiuter� a programmare una semplice interfaccia per l'utente in cui si
ha la possibilità  a scegliere le immagini attuali del programma oppure
un'altra immagine scelta dall'utente.
"""

# importo delle libreri necessarie


from models.jpeg import Jpeg as j
from sys import exit
import time


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

    j.display(image)

    dim = input("Scegliere la dimensione di taglio immagine:\t")

    j.cutImage(image, int(dim))

    f = input("Scegliere la dimensione del blocco F:\t")

    d = input("Scegliere il taglio d tra [0: 2F-2]:\t")

    j.dctEncode(image, int(dim), int(f), int(d))

    j.idctDecode(image, int(dim), int(f), int(d))

    end = time.perf_counter()

    j.compare(image)