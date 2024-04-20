
# PROGRAMMA DI TEST 2

import pandas as pd
import Test1

# A partire dalla lista delle imprese ottenuta leggendo il file “imprese_ordinate.txt” generato in precedenza
# ed utilizzando opportune funzioni ausiliarie, vengono implementati i metodi a seguire.

#######################################################################################################################################################################
# MAIN 
#######################################################################################################################################################################

def main ():
    # lettura file .txt con l'array di imprese
    arrayImprese = Test1.leggiImprese("imprese_ordinate.txt")
    
    print(f"Media aritmetica tra Numero di Soci e Numero di Dipendenti per ciascuna impresa:\n{calcoloMediaAritmetica(arrayImprese)}\n")
    
    print(f"Medie di Dipendenti e Soci tra tutte le imprese:\n{calcoloMediaAritmetica2(arrayImprese)}\n")

    print(f"Percentuale di imprese in possesso di Certificazioni di Qualità con fatturato annuale tra 10.000 e 50.000 €:\n{percentualeImprese(arrayImprese)}%\n")

    print(f"Aziende del tipo 'Società di Capitale' in possesso di Certificazioni di Qualità:\n{QualitaCapitale(arrayImprese)}\n")
    
    print(f"Numero di imprese per divisione ATECO:\n{numeroATECO(arrayImprese)}\n")


#######################################################################################################################################################################
# FUNCTIONS 
#######################################################################################################################################################################

# calcoloMediaAritmetica(arrayImprese) calcola, per ciascuna impresa, la media tra il suo numero di soci e il suo numero di dipendenti.
# Resitutisce un array con il nome e il codice fiscale di ciascuna impresa, associati a tale media.

def calcoloMediaAritmetica (arrayImprese):
    arrayMedie = [] # dichiarazione di un array vuoto che una volta riempito avrà questo aspetto: {Callipo, 37, Enel, 29, Fiat, 94, etc.}
    
    for impresa in arrayImprese:
        
        # Calcolo della media aritmetica
        mediaAritmetica = (impresa.numeroDipendenti + impresa.numeroSoci) / 2

        # Dizionario con i dati anagrafici dell'impresa e la media aritmetica
        mediaAritmeticaDict = {
            "Codice Fiscale": impresa.codiceFiscale,
            "Nome Impresa": impresa.Denominazione,
            "Media Dipendenti e Soci": mediaAritmetica
            }

        # Aggiunta del dizionario all'array
        arrayMedie.append(mediaAritmeticaDict)
    return arrayMedie

#######################################################################################################################################################################

# "calcoloMediaAritmetica2(arrayImprese)" calcola DUE medie aritmetiche:
# 1) la media del numero di dipendenti tra tutte le imprese nel txt
# 2) la media del numero di soci tra tutte le imprese nel txt
# Resitutisce i due valori.

def calcoloMediaAritmetica2 (arrayImprese):
    totDipendenti = 0
    totSoci = 0
    count = 0
    for impresa in arrayImprese:
        totDipendenti += impresa.numeroDipendenti
        totSoci += impresa.numeroSoci
        count +=1
    if count == 0:
        raise ValueError ("L'array di imprese è vuoto.")
    return{
        "Media dei dipendenti:": totDipendenti/count,
        "Media dei soci:": totSoci/count
        }        

#######################################################################################################################################################################

# percentualeImprese (arrayImprese) calcola la percentuale di imprese con “Certificazioni di qualità” o “Fatturato” compreso tra 10000 e 50000 Euro (estremi compresi)

def percentualeImprese (arrayImprese):
    count = 0
    totImprese = 0
    for impresa in arrayImprese:
        if impresa.certificazioneQualita or 10000<impresa.Fatturato<50000: # ricordare il true se dà errore
            count +=1
        totImprese +=1
    if totImprese == 0:
        print ("L'array di imprese è vuoto.")
        return 0
    return (count/totImprese) * 100

#######################################################################################################################################################################

# QualitaCapitale (arrayImprese) stampa un elenco dei nomi delle aziende con certificazioni di qualità (“Certificazioni di qualità” == True) e “Ragione Sociale” = Società di Capitale
# il metodo utilizza pandas.

def QualitaCapitale (arrayImprese):
    newDataFrame = pd.DataFrame([(impresa.Denominazione, impresa.certificazioneQualita, impresa.ragioneSociale) for impresa in arrayImprese],
        columns=["Nome impresa","Certificazioni di qualità impresa", "Ragione Sociale impresa"])
    
    arrayFiltrato = newDataFrame[(newDataFrame["Certificazioni di qualità impresa"] == True) & (newDataFrame["Ragione Sociale impresa"] == "Societa di Capitale")] 
    
    nomiImprese = []
    for Denominazione in arrayFiltrato["Nome impresa"]:
        nomiImprese.append(Denominazione)

    arrayNomiImprese = ", ".join(nomiImprese)
    return arrayNomiImprese

#######################################################################################################################################################################

# numeroATECO (arrayImprese) conta il numero di aziende appartenenti a ciascuna divisione ATECO

def numeroATECO (arrayImprese):
    count = {}  # Dizionario per conteggi ATECO
    for impresa in arrayImprese:
        ateco = impresa.divisioneAteco
        if ateco not in count:
            count[ateco] = 0
        count[ateco] +=1
    return count

#######################################################################################################################################################################

if __name__ == "__main__":
    main()