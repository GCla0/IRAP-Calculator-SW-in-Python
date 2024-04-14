
# PROGRAMMA DI TEST 1

# Legga dal file di testo “imprese.txt” (da creare opportunamente con un editor di testo e contenente
# almeno i dati di 8 imprese) l’insieme delle imprese e li memorizzi, come oggetti di tipo “Impresa”,
# all’interno di una lista;

from Classes import Impresa # importazione classe impresa
from datetime import datetime # formato data 

def leggiImprese():
    arrayImprese = [] #dichiaro array vuoto che ospiterà gli oggetti di tipo impresa
    try: # verifica della presenza del file
        with open("imprese.txt", "r") as file: 
            for riga in file:
                dati = riga.split(",")
                impresa = Impresa(
                    dati[0], # codice fiscale
                    dati[1], # denominazione
                    dati[2], # ragione sociale
                    dati[3], # divisione ATECO
                    int(dati[4]), # numero di dipendenti
                    int(dati[5]), # numero di soci
                    int(dati[6]), # numero di amministratori
                    datetime.strptime(dati[7],"%d-%m-%Y"), # data di costituzione (in formato datatime)
                    bool(dati[8].lower()=="true"), # certificazione di qualità (booleano)
                    int(dati[9]) # fatturato annuale
                )
                arrayImprese.append(impresa) #Aggiungo l'oggetto Impresa all'array lista_imprese
    except FileNotFoundError as E: # se file assente
        print(E)
    return arrayImprese

# A partire dalla lista delle imprese, crei un dizionario contenente per ogni “Codice Fiscale” il totale di
# persone coinvolte nell’impresa, cioè la somma di “Numero di dipendenti”, “Numero di soci”, e
# “Numero di amministratori”;

def creaDizionarioPersoneCoinvolte(arrayImprese):
  DizionarioPersoneCoinvolte = {}

  for impresa in arrayImprese:
    TotalePersoneCoinvolte = impresa.numeroDipendenti + impresa.numeroSoci + impresa.numeroAmministratori

    if impresa.codiceFiscale in DizionarioPersoneCoinvolte:
      # Se il codice fiscale esiste, aggiorna il totale
      DizionarioPersoneCoinvolte[impresa.codiceFiscale] += TotalePersoneCoinvolte
    else:
      # Se il codice fiscale non esiste, lo aggiunge al dizionario
      DizionarioPersoneCoinvolte[impresa.codiceFiscale] = TotalePersoneCoinvolte

  return DizionarioPersoneCoinvolte

# Ordini la lista delle imprese per “Divisione ATECO” (seguendo l’ordine alfabetico) e a parità di
# “Divisione ATECO” per “Numero di amministratori” (in ordine decrescente);

def ordinaImprese(arrayImprese):
    arrayImprese.sort(key=lambda x: (x.divisioneAteco, -x.numeroAmministratori)) 
    return arrayImprese

# Visualizzi i dati di tutte le imprese presenti nella lista;
def visualizzaImprese(arrayImprese):
   for impresa in arrayImprese:
      print(f"Codice fiscale: {impresa.codiceFiscale}; Denominazione: {impresa.Denominazione}; Ragione sociale: {impresa.ragioneSociale}; Divisione ATECO: {impresa.divisioneAteco}; Numero dipendenti: {impresa.numeroDipendenti}; Numero soci: {impresa.numeroSoci}; Numero amministratori: {impresa.numeroAmministratori}; Data di costituzione: {impresa.dataCostituzione.strftime("%d-%m-%Y")}; Certificazione di qualità: {impresa.certificazioneQualita}; Fatturato: {impresa.Fatturato}\n")

# Salvi sul file “imprese_ordinate.txt” il contenuto finale della lista
def scriviImprese(arrayImprese):
    with open ("imprese_ordinate.txt", "w") as file:
        for impresa in arrayImprese:
            file.write (f"{impresa.codiceFiscale},{impresa.Denominazione},{impresa.ragioneSociale},{impresa.divisioneAteco},{impresa.numeroDipendenti},{impresa.numeroSoci},{impresa.numeroAmministratori},{impresa.dataCostituzione.strftime("%d-%m-%Y")},{impresa.certificazioneQualita},{impresa.Fatturato}\n") 

#######################################################################################################################################################################
# MAIN 
#######################################################################################################################################################################

def main ():
    # lettura file .txt con l'array di imprese
    arrayImprese = leggiImprese()
    
    # creazione e visualizzazione del dizionario
    dizionario = creaDizionarioPersoneCoinvolte(arrayImprese)
    print(dizionario)
    print("\n")

    #ordinamento e visualizzazione di un nuovo array di imprese in ordine di divisione ATECO
    arrayImpreseOrdinate = ordinaImprese(arrayImprese)
    visualizzaImprese(arrayImpreseOrdinate)
    
    # salvataggio nuovo array su file .txt
    scriviImprese(arrayImpreseOrdinate)

if __name__ == "__main__":
    main()