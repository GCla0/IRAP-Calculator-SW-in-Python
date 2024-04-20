
# PROGRAMMA DI TEST 1

from Classes import Impresa # importazione classe impresa
from datetime import datetime # formato data 

#######################################################################################################################################################################
# MAIN 
#######################################################################################################################################################################

def main ():
    # lettura file .txt con l'array di imprese
    arrayImprese = leggiImprese("imprese.txt")

    # creazione e visualizzazione del dizionario
    dizionario = creaDizionarioPersoneCoinvolte(arrayImprese)
    print(f"Dizionario:\n{dizionario}\n")
    
    # ordinamento e visualizzazione di un nuovo array di imprese in ordine di divisione ATECO
    arrayImpreseOrdinate = ordinaImprese(arrayImprese)
    print("Lista delle imprese a sistema ordinate per divisione ATECO:\n")
    visualizzaImprese(arrayImpreseOrdinate)
    
    # salvataggio nuovo array su file .txt
    scriviImprese(arrayImpreseOrdinate)


#######################################################################################################################################################################
# FUNCTIONS 
#######################################################################################################################################################################

# leggiImprese(txt) legge il file di testo “imprese.txt” e li registra a sistema come oggetti di tipo Impresa

def leggiImprese(txt):
    arrayImprese = [] #dichiarazione di un array vuoto che ospiterà gli oggetti di tipo impresa

    # verifica della presenza del txt nella directory
    try: 
        with open(txt, "r") as file: 
            for riga in file:
                dati = riga.split(",")
                impresa = Impresa(
                    dati[0],                                # codice fiscale
                    dati[1],                                # denominazione
                    dati[2],                                # ragione sociale
                    dati[3],                                # divisione ATECO
                    int(dati[4]),                           # numero di dipendenti
                    int(dati[5]),                           # numero di soci
                    int(dati[6]),                           # numero di amministratori
                    datetime.strptime(dati[7],"%d-%m-%Y"),  # data di costituzione (in formato datatime)
                    bool(dati[8].lower()=="true"),          # certificazione di qualità (si o no == true or false)
                    int(dati[9])                            # fatturato annuale
                )
                if impresa not in arrayImprese: 
                    arrayImprese.append(impresa) # esclusivamente se l'impresa non è stata ancora aggiunta all'array, viene inserita
    except FileNotFoundError as E: # caso in cui il txt non fosse nella directory
        print(E)
    return arrayImprese

#######################################################################################################################################################################

# creaDizionarioPersoneCoinvolte(arrayImprese) crea un dizionario contenente per ogni “Codice Fiscale” il totale di persone coinvolte nell’impresa (dipendenti+soci+amministratori)

def creaDizionarioPersoneCoinvolte(arrayImprese):
  DizionarioPersoneCoinvolte = {}

  for impresa in arrayImprese:
    TotalePersoneCoinvolte = impresa.numeroDipendenti + impresa.numeroSoci + impresa.numeroAmministratori

    if impresa.codiceFiscale in DizionarioPersoneCoinvolte:
      # Se il codice fiscale esiste, aggiorna il totale
      DizionarioPersoneCoinvolte[impresa.codiceFiscale] += TotalePersoneCoinvolte
    else:
      # Se il codice fiscale NON esiste, viene aggiunto al dizionario
      DizionarioPersoneCoinvolte[impresa.codiceFiscale] = TotalePersoneCoinvolte

  return DizionarioPersoneCoinvolte

#######################################################################################################################################################################

# ordinaImprese(arrayImprese) ordina la lista delle imprese per “Divisione ATECO” (seguendo l’ordine alfabetico) e a parità di “Divisione ATECO” per “Numero di amministratori” (in ordine decrescente)

def ordinaImprese(arrayImprese):
    arrayImprese.sort(key=lambda x: (x.divisioneAteco, -x.numeroAmministratori)) 
    return arrayImprese

#######################################################################################################################################################################

# visualizzaImprese(arrayImprese) stampa i dati di tutte le imprese presenti nella lista

def visualizzaImprese(arrayImprese):
   for impresa in arrayImprese:
      print(f"Codice fiscale: {impresa.codiceFiscale}; Denominazione: {impresa.Denominazione}; Ragione sociale: {impresa.ragioneSociale}; Divisione ATECO: {impresa.divisioneAteco}; Numero dipendenti: {impresa.numeroDipendenti}; Numero soci: {impresa.numeroSoci}; Numero amministratori: {impresa.numeroAmministratori}; Data di costituzione: {impresa.dataCostituzione.strftime("%d-%m-%Y")}; Certificazione di qualità: {impresa.certificazioneQualita}; Fatturato: {impresa.Fatturato}\n")

#######################################################################################################################################################################

# scriviImprese(arrayImprese) salva sul file “imprese_ordinate.txt” il contenuto finale della lista

def scriviImprese(arrayImprese):
    with open ("imprese_ordinate.txt", "w") as file:
        for impresa in arrayImprese:
            file.write (f"{impresa.codiceFiscale},{impresa.Denominazione},{impresa.ragioneSociale},{impresa.divisioneAteco},{impresa.numeroDipendenti},{impresa.numeroSoci},{impresa.numeroAmministratori},{impresa.dataCostituzione.strftime("%d-%m-%Y")},{impresa.certificazioneQualita},{impresa.Fatturato}\n") 

#######################################################################################################################################################################

if __name__ == "__main__":
    main()