
# PROGRAMMA DI TEST 3

from datetime import date, datetime
from time import strptime
from Classes import Impresa, Comune, calcolaIrap
import Test1

# Implementare un terzo programma di test che:
# Crea uno o più comuni

def creaImpresa (arrayImprese):
    # nel main verrà dato in input l'output della funzione leggiImprese(txt) perché aggiunga le nuove alle preesistenti
    codiceFiscale = input("Si digiti il Codice Fiscale dell'impresa: ")
    for impresa in arrayImprese:
        if codiceFiscale == impresa.codiceFiscale:
            print("Questa impresa è già stata registrata a sistema.") # l'assunzione è che il codice fiscale sia univoco
            return
    Denominazione = input("Si digiti il nome dell'impresa: ")
    ragioneSociale = input("Si digiti la ragione sociale dell'impresa: ")
    divisioneAteco = input("Si digiti la divisione ATECO dell'impresa: ")
    numeroDipendenti = int(input("Si digiti il numero di dipendenti dell'impresa: "))
    numeroSoci = int(input("Si digiti il numero di soci dell'impresa: "))
    numeroAmministratori = int(input("Si digiti il numero di amministratori dell'impresa: "))
    dataCostituzione = datetime.strptime(input("Si digiti la data di costituzione dell'impresa (in formato DD-MM-YYYY): "),"%d-%m-%Y")
    certificazioneQualita = input("L'impresa dispone di certificazioni di qualità? (Y/N)")
    certificazioneQualita = bool(certificazioneQualita.lower() in ["Y"])
    Fatturato = int(input("Si digiti il fatturato annuale dell'impresa: "))
    
    nuovaImpresa = Impresa(codiceFiscale,Denominazione,ragioneSociale,divisioneAteco,numeroDipendenti,numeroSoci,numeroAmministratori,dataCostituzione,certificazioneQualita,Fatturato)
    arrayImprese.append(nuovaImpresa)
    print(f"Impresa '{Denominazione}' creata a sistema.")
    return arrayImprese

def creaComune (arrayComuni):
    # nel main verrà dato in input l'output della funzione leggiComuni(txt) perché aggiunga i nuovi ai preesistenti
    nome = input("Si digiti il nome del comune: ")
    for comune in arrayComuni:
        if nome == comune.nome:
            print("Questo Comune è già stato registrato a sistema.") # si assume che non esistano comuni omonimi
            return
    regione = input("Si digiti la regione a cui appartiene il comune: ")
    abitanti = int(input("Si digiti il numero di abitanti del comune: "))
    
    nuovoComune = Comune(nome,regione,abitanti)
    arrayComuni.append(nuovoComune)
    print(f"Comune di {nuovoComune.nome} creato a sistema.")
    
    return arrayComuni

def leggiComuni(txt):
    arrayComuni = [] #dichiarazione di un array vuoto che ospiterà gli oggetti di tipo Comune
    try: # verifica della presenza del txt nella directory
        with open(txt, "r") as file: 
            for riga in file:
                dati = riga.split(",")
                comune = Comune(
                    dati[0], # nome
                    dati[1], # regione
                    int(dati[2])) # numero di abitanti
                
                if comune not in arrayComuni: # esclusivamente se il comune non è stato ancora aggiunta all'array
                    arrayComuni.append(comune)

    except FileNotFoundError as E: # caso in cui il txt non fosse nella directory
        print(E)
    return arrayComuni

# Effettua la registrazione di un’impresa presso il comune

def registrazioneIC(arrayImprese, arrayComuni):
    codiceFiscale = input("Si digiti il Codice Fiscale dell'impresa da registrare: ")
    
    # controllo 1: esistenza dell'impresa a sistema
    foundI=0
    for impresa in arrayImprese:
        if codiceFiscale == impresa.codiceFiscale:
            foundI = impresa        
    if foundI==0:
        print("L'impresa deve essere creata a sistema.")
        return
    
    # controllo 2: che l'impresa non sia registrata presso altro comune
    for comune in arrayComuni:
        for impresa in comune.impreseRegistrate:
            if codiceFiscale == impresa.codiceFiscale:
                print(f"L'impresa {impresa.Denominazione} è già registrata presso il comune di {comune.nome}.")
                return
    
    # se l'impresa esiste a sistema e non è ancora stata registrata presso nessun comune...
    nomeComune = input("Presso quale comune si vuole registrare l'impresa? ")
    foundC=0
    for comune in arrayComuni:
        if nomeComune == comune.nome:
            foundC = comune
            foundC.registraImpresa(foundI)
            print(f"Impresa '{foundI.Denominazione}' registrata presso il comune di {foundC.nome}.")
            break
    if foundC==0:
        print("Il comune deve essere creato a sistema.")
        return

# Calcoli l’import IRAP per l’impresa

def IRAP(arrayImprese):
    cf = input("Si digiti il Codice Fiscale dell'impresa per cui si vuole conoscere la quota IRAP: ")
    for impresa in arrayImprese:
        if cf == impresa.codiceFiscale:
            print(f"Quota IRAP per l'impresa {impresa.Denominazione}: {calcolaIrap(impresa)} €.")
            return #calcolaIrap(impresa)
    print ("Il Codice Fiscale inserito non corrisponde a nessuna impresa registrata a sistema.")
    return

# Emissione del modello F24 per l’impresa da parte del comune

def emissione(arrayImprese, arrayComuni):
    cf = input("Si digiti il Codice Fiscale dell'impresa per cui si vuole emettere il Modello F24: ")
    exit=False
    for impresa in arrayImprese:
        if impresa.codiceFiscale==cf:
            exit=True
    if exit==False:
        print ("Il Codice Fiscale inserito non corrisponde a nessuna impresa registrata a sistema.")
        return

    # e se l'impresa esiste a sistema... 
    for comune in arrayComuni:
        listaImpreseRegistrate= comune.impreseRegistrate
        for impresa in listaImpreseRegistrate:
            if cf==impresa.codiceFiscale:
                today = date.today()
                today = today.strftime("%d-%m-%Y") 
                today = datetime.strptime(today, "%d-%m-%Y")
                return comune.emettiModelloF24(impresa, today)
    print ("L'impresa selezionata non è registrata presso nessun comune.")
    return

# Stampa dei modelli F24 emessi dal comune

def stampaModelli(arrayComuni):
    dove = input("Si digiti il nome del Comune di cui si vogliono visualizzare i Modelli F24 emessi: ")
    for comune in arrayComuni:
        if dove == comune.nome:
            if len(comune.modelliF24Emessi)==0:
                print("Non esistono Modelli F24 emessi da questo comune.")
                return
            print(f"Modelli F24 emessi dal comune di {dove}:")
            for modello in comune.modelliF24Emessi:
                print(f"\n{modello.preparaF24()}")
            return
    print ("Il nome inserito non corrisponde a nessun Comune registrato a sistema.")
    return

# Generazione di un report con statistiche sull’importo totale dell’IRAP riscosso dal comune in un determinato periodo di tempo.
# Con aggiunta di un modello che consente di registrare a sistema Modelli F24 emessi nel passato.

def antichiModelliF24(arrayImprese,arrayComuni):
    cf = input("Si digiti il Codice Fiscale dell'impresa per cui si vuole registrare un antico Modello F24: ")
    exit=False
    for impresa in arrayImprese:
        if cf == impresa.codiceFiscale:
            exit=True
            break
    if exit==False:
        print("L'impresa deve essere creata a sistema.")
        return
    
    # e se l'impresa esiste a sistema...
    
    for comune in arrayComuni:
        listaImpreseRegistrate= comune.impreseRegistrate
        for impresa in listaImpreseRegistrate:
            if cf==impresa.codiceFiscale:
                data = vecchiaData()
                return comune.emettiModelloF24(impresa, data)
        print("L'impresa selezionata non è registrata presso nessun comune.")
        return

# Il metodo 'vecchiaData()' verifica che la data inserita in input da tastiera sia anteriore a quella odierna

def vecchiaData ():
    exit=False
    while exit==False:
        exit=True
        try:
            data = input("Si digiti la data di emissione (anteriore alla data odierna) del Modello F24 che si vuole registrare (in formato DD-MM-YYYY): ")
            data = datetime.strptime(data,"%d-%m-%Y")
            data_oggi = date.today()
            data_oggi = data_oggi.strftime("%d-%m-%Y")
            if data >= datetime.strptime(data_oggi,"%d-%m-%Y"):
                exit=False
                print("Data inserita non valida.")    
        except ValueError:
            exit=False
    return data

def report(arrayComuni):
    dove = input("Si digiti il nome del Comune di cui si vuole visualizzare un report: ")
    exists=False
    for comune in arrayComuni:
        if dove == comune.nome:
            arrayModelli=comune.modelliF24Emessi
            if len(comune.modelliF24Emessi) == 0:
                print(f"Il comune di {dove} non ha rilasciato nessun ModelloF24.")
                return
            else:
                start = input("Si digiti la data di inizio del periodo da verificare (in formato DD-MM-YYYY):")
                start = datetime.strptime(start,"%d-%m-%Y")
                end = input("Si digiti la data di fine del periodo da verificare (in formato DD-MM-YYYY):")
                end = datetime.strptime(end,"%d-%m-%Y")
                exists=True
                break
    if exists==False:
        print(f"Il comune di {dove} non è registrato a sistema.")
        return
    
    # se il comune esiste a sistema e ci sono dei modelli emessi registrati...
    
    count = 0 # per contare quante imprese hanno emesso i ModelliF24 presso il comune dato in input
    sum = 0 # per sommare l'importo totale dell'IRAP
    reportImprese = [] # array in cui verranno inseriti oggetti di tipo impresa che hanno emesso un ModelloF24 presso il comune dato in input
    
    for modello in arrayModelli:
        if modello.dataModello >= start and modello.dataModello <= end: 
            reportImprese.append(modello.impresa)
            sum += modello.importoIrap
            count +=1

    DizionarioRagioneSociale = {}
    DizionarioCount ={}

    for modello in arrayModelli:
        
        if modello.impresa.ragioneSociale in DizionarioRagioneSociale:
            # Se la ragione sociale esiste, aggiorna il totale
            DizionarioCount[modello.impresa.ragioneSociale] += 1
            DizionarioRagioneSociale[modello.impresa.ragioneSociale] += (modello.impresa.Fatturato/DizionarioCount[modello.impresa.ragioneSociale])
        else:
            # Se il codice fiscale NON esiste, viene aggiunto al dizionario
            DizionarioCount[modello.impresa.ragioneSociale] = 1
            DizionarioRagioneSociale[modello.impresa.ragioneSociale] = (modello.impresa.Fatturato/DizionarioCount[modello.impresa.ragioneSociale])

    
    # lista delle imprese registrate presso il comune
    print(f"Imprese registrate presso il comune di {dove}: {listaRegistrazioni}")
    # IRAP totale riscosso dal comune richiesto
    print(f"Importo IRAP totale riscosso dal comune di {dove} nel periodo selezionato: {sum} €\n")
    # media dell'IRAP riscosso da tutte le aziende del comune richiesto
    print(f"Media importo IRAP per impresa riscosso dal comune di {dove} nel periodo selezionato: {sum/count} €\n")
    # media IRAP riscosso da tutte le aziende del comune richiesto, suddivise per ragione sociale
    print(f"Media importo IRAP per Ragione Sociale riscosso dal comune di {dove} nel periodo selezionato:\n{DizionarioRagioneSociale}\n")  
    
def listaRegistrazioni(arrayComuni):
    aqui = input("Si digiti il nome del Comune presso cui si vogliono consultare le imprese registrate: ")
    found=False
    for comune in arrayComuni:
        if aqui == comune.nome:
            if len(comune.impreseRegistrate) ==0:
                print(f"Presso il comune di {aqui} non risulta alcuna impresa registrata.")
                return
            else:
                found=True
                print(f"Imprese registrate presso il comune di {aqui}:")
                for impresa in comune.impreseRegistrate:
                    print (impresa.Denominazione)
                return
    if found == False:
        print(f"Il comune di {aqui} non è registrato a sistema.")
        return
        
#######################################################################################################################################################################
# MAIN 
#######################################################################################################################################################################

def main ():
    # lettura file .txt con l'array di comuni
    arrayComuni = leggiComuni("comuni.txt")
    # lettura file .txt con l'array di imprese
    arrayImprese = Test1.leggiImprese("imprese_ordinate.txt")
    exit=False
    while (exit == False):
        
        value = input("Operazioni disponibili: \n 1: Creazione Report per Comune \n 2: Calcolo quota IRAP per Impresa \n 3: Emissione e Registrazione nuovo Modello F24 \n 4: Registrazione Modello F24 precedentemente emesso \n 5: Lista Modelli F24 \n 6: Inserimento Comune \n 7: Inserimento Impresa \n 8: Registrazione Impresa-Comune \n 9: Lista Imprese registrate presso Comune \n 10: Fine operazioni \n")
        
        match value:
            case "1": #Creazione Report per Comune
                report(arrayComuni)

            case "2": #Calcolo quota IRAP per l'impresa
                #return IRAP(arrayImprese)
                IRAP(arrayImprese)

            case "3": #Emissione e Registrazione nuovo Modello F24
                emissione(arrayImprese,arrayComuni)

            case "4": #Registrazione Modello F24 precedentemente emesso
                antichiModelliF24(arrayImprese,arrayComuni)

            case "5": #Lista Modelli F24
                stampaModelli(arrayComuni) 

            case "6": #Inserimento Comune
                arrayComuni = creaComune(arrayComuni)

            case "7": #Inserimento Impresa
                arrayImprese = creaImpresa(arrayImprese)

            case "8": #Registrazione Impresa-Comune
                registrazioneIC(arrayImprese, arrayComuni)

            case "9": #Visualizzare la lista di imprese registrate presso un comune
                listaRegistrazioni(arrayComuni)

            case "10": #Fine operazioni
                exit = True

            case _:
                print("Scegliere un'operazione tra le alternative da 1 a 10.")
    
if __name__ == "__main__":
    main()