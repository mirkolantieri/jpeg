# Compressione di immagini tramite la DCT
## Progetto Metodi del Calcolo Scientifico
### A.A 2019/2020
***
<div>
<i><b>LANTIERI MIRKO</b></i>
<br>Matricola 858278
<br>Email: m.lantieri@campus.unimib.it
</div>

***
# 1. Introduzione

<p>
Nel seguente progetto di <i>'Metodi del Calcolo Scientifico'</i> viene mostrato com'è possibile
effettuare la DCT (Discrete Cosine Transform) utilizzando ambienti open-source, in modo tale 
da poter confrontare, quale ambiente sia il migliore, ossia il mondo <b>"Open" </b> o quello <b>"Closed"</b> 
(come ad esempio <b> Matlab &copy; </b>).
L'ambiente open source utilizzato come un possibile avversario potenziale di Matlab,
è quello di <b>Python</b>, nello specifico il framework <b>Anaconda3</b>.
<br>
Nel caso si riscontra qualche problema nell'importare il progetto nel proprio
ambiente IDE (utilizzare Spyder), guardare il testo <i>"requirements.txt"</i> per risolvere eventuali conflitti. 
</p>

## 1.1 Dati e codice sorgente
Nel progetto le immagini utilizzate sono cinque, ritrovabili anche nel folder _/data_
del progetto. Quest'ultime rappresentano alcuni personaggi famosi della saga dei film di 
_**Star Wars (Guerre Stellari)**_ scelte solo per puro piacimento personale,
 ma qualsiasi immagine può andare perfettamente
per lo scopo del progetto, dal fatto che:
 1. Sono salvate in formato `.bmp`, perché si vuole comprendere il passaggio
 di compressione in formato `.jpeg` , quindi non avrebbe senso il contrario.
 2. Le immagini risiedono di colori monocromatici, cioè sono appositamente scelte in bianco e nero,
 da poter evitare la conversione `RGB` in `BW`.
 3. L'utente ha comunque la possibilità di scegliere immagini a suo piacimento
 oltre a quelle predefinite nel progetto.
 
Per quanto riguarda il codice sorgente, esso è caricato nel folder `/models` e contiene
la nostra libreria "fatta in casa" per quanto riguarda le trasformate. Il file
della libreria si chiama: `jpeg.py`.
 Il file `main.py` contiene l'interfaccia interagente con l'utente, utilizzabile nel caso
 si preferisce un altra immagine tra quelle predefinite nel folder `/data`.
 
# 2. Immagini

Le immagini utlizzate si trovano nel folder data:

1. Baby Yoda: [logo](/data/BabyYoda.bmp "BabyYoda.bmp")
2. C3PO: [logo](/data/BenKenobi.bmp "C3PO.bmp")
3. Darth Vader Death Star: [logo](/data/DarthVader_DeathStar.bmp "DarthVader_DeathStar.bmp")
4. Darth Vader: [logo](/data/DarthVader.bmp "DarthVader.bmp")
5. Millenium Falcon: [logo](/data/MilleniumFalcon.bmp "MilleniumFalcon.bmp")

# 3. Libreria Jpeg (Custom)
La libreria `Jpeg` si trova nel folder `models/` ed è composta da seguenti metodi:

 ```python
 # Costruttore: inizializza l'oggetto
    def __init__(self):
        return 
```