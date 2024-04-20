# Classes.py
# Classe Impresa, Comune e ModelloF24 con associati metodi.

from datetime import datetime

class Impresa:
    def __init__(self, codiceFiscale, Denominazione, ragioneSociale, divisioneAteco, numeroDipendenti, numeroSoci, numeroAmministratori, dataCostituzione, certificazioneQualita, Fatturato):
        self.codiceFiscale = codiceFiscale                  # il codice fiscale dell'impresa
        self.Denominazione = Denominazione                  # nome dell'impresa
        self.ragioneSociale = ragioneSociale                # tipo di società
        self.divisioneAteco = divisioneAteco                # divisione ATECO in cui opera l'impresa (e.g. A01, A02, …, B05)
        self.numeroDipendenti = numeroDipendenti            # numero di dipendenti
        self.numeroSoci = numeroSoci                        # numero di soci
        self.numeroAmministratori = numeroAmministratori    # numero di amministratori
        self.dataCostituzione = dataCostituzione            # data in cui è stata costituita l'azienda, in formato DD-MM-YYYY
        self.certificazioneQualita = certificazioneQualita  # vale True se l’impresa ha certificazioni di qualità, False altrimenti
        self.Fatturato = Fatturato                          # fatturato annuo dell'impresa

def calcolaIrap(self):
        # Determinazione dell'aliquota IRAP e del coefficiente per le imprese sulla base del fatturato annuo

        if self.Fatturato < 10000:         # Se il fatturato è minore di 10.000€, aliquota IRAP e coefficiente sono 0
            aliquota = 0
            coefficiente = 0
        elif self.Fatturato < 50000:       # Prima fascia
            aliquota = 0.0049
            coefficiente = 1.2
        elif self.Fatturato < 150000:      # Seconda fascia
            aliquota = 0.0076
            coefficiente = 1.5
        else:                              # Terza fascia
            aliquota = 0.0081
            coefficiente = 1.7

        # Calcolo dell'IRAP lorda con applicazione aliquota IRAP e coefficiente 
        calcolo_coefficiente = self.Fatturato * coefficiente
        irap_lorda = calcolo_coefficiente * aliquota

        # Riduzione IRAP per imprese agevolate
        riduzione = 0  # inizializzazione a 0 della quota di agevolazione
        if dirittoAgevolazione(self) == True:
            riduzione = irap_lorda * 1.5 / 100
        # Calcolo dell'IRAP netta
        totale_irap = irap_lorda - riduzione
        return totale_irap


def dirittoAgevolazione(self): 
        # Verifica se l'impresa in esame è avente o no diritto a un'agevolazione sull'IRAP.
        # In altre parole, verifica se la divisione ATECO è "A03" e se il numero di dipendenti è maggiore di 15.

        if self.divisioneAteco == "A03" and self.numeroDipendenti > 15:
            return True
        else:
            return False
        
#######################################################################################################################################################################

class Comune:
    def __init__(self, nomeComune, regione, abitanti):
        self.nome = nomeComune
        self.regione = regione
        self.abitanti = abitanti
        self.impreseRegistrate = []     # Array di imprese registrate presso il comune
        self.modelliF24Emessi = []      # Array dei Modelli F24 emessi presso il comune

    # Metodo per registrare un'impresa presso il comune

    def registraImpresa(self, impresa):  
        self.impreseRegistrate.append(impresa)

    # Metodo per emettere un Modello F24 presso il comune

    def emettiModelloF24(self, impresa, data):
        # per prima cosa si controlla che la stessa impresa non abbia già emesso un modello nella stessa data presso questo comune
        for mod in self.modelliF24Emessi:
            if data == mod.dataModello:
                print(f"Un Modello F24 è già stato emesso da quest'impresa in questa data.")
                return
        modelloF24 = ModelloF24(impresa, data)              # Creazione di un nuovo oggetto di tipo ModelloF24 con relativa impresa
        self.modelliF24Emessi.append(modelloF24)            # Aggiunta di tale Modello F24 alla lista dei modelli emessi dal 
        print(f"Modello F24 per l'impresa '{impresa.Denominazione}' emesso presso il comune di {self.nome}.")

#######################################################################################################################################################################

class ModelloF24:
    def __init__(self, impresa, dataModello):
        self.impresa = impresa 
        self.dataModello = dataModello
        #dataModello = datetime.strptime(dataModello,"%d-%m-%Y") #questo dà errore
        self.importoIrap = calcolaIrap(impresa)

    # Metodo per preparare e visualizzare il Modello F24 per l'impresa, utilizzando l'importo dell'IRAP calcolato
    def preparaF24(self):
        return {
            "Codice Fiscale dell'impresa": self.impresa.codiceFiscale,
            "Nome dell'impresa": self.impresa.Denominazione,
            "Ragione Sociale dell'impresa": self.impresa.ragioneSociale,
            "Divisione ATECO dell'impresa": self.impresa.divisioneAteco,
            "Data di costituzione dell'impresa": self.impresa.dataCostituzione.strftime("%d-%m-%Y"),
            "Possesso di certificazioni di qualità": self.impresa.certificazioneQualita,
            "Quota IRAP": self.importoIrap,
            "Data emissione modello": self.dataModello.strftime("%d-%m-%Y")
        }