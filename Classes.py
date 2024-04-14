class Impresa:
    def __init__(self, codiceFiscale, Denominazione, ragioneSociale, divisioneAteco, numeroDipendenti, numeroSoci, numeroAmministratori, dataCostituzione, certificazioneQualita, Fatturato):
        self.codiceFiscale = codiceFiscale #il codice fiscale dell’azienda
        self.Denominazione = Denominazione # nome dell'azienda
        self.ragioneSociale = ragioneSociale # tipo di società
        self.divisioneAteco = divisioneAteco # divisione ATECO in cui opera l’azienda (es. A01, A02, …, B05)
        self.numeroDipendenti = numeroDipendenti
        self.numeroSoci = numeroSoci
        self.numeroAmministratori = numeroAmministratori
        self.dataCostituzione = dataCostituzione
        self.certificazioneQualita = certificazioneQualita #vale True se l’impresa ha certificazioni di qualità; False altrimenti.
        self.Fatturato = Fatturato #annuo

def calcolaIrap(self):
        #Determinazione dell'aliquota IRAP e del coefficiente per le imprese sulla base del faturato
        if self.fatturato < 10000: #Se il fatturato è minore di 10.000€, aliquota IRAP e coefficiente sono 0
            aliquota = 0
            coefficiente = 0
        elif self.fatturato < 50000:
            aliquota = 0.0049
            coefficiente = 1.2
        elif self.fatturato < 150000:
            aliquota = 0.0076
            coefficiente = 1.5
        else:
            aliquota = 0.0081
            coefficiente = 1.7

        #Calcolo dell'IRAP lorda con applicazione aliquota IRAP e coefficiente 
        calcolo_coefficiente = self.fatturato * coefficiente
        irap_lorda = calcolo_coefficiente * aliquota

        #Riduzione IRAP per imprese agevolate
        riduzione = 0  
        if Impresa.dirittoAgevolazione(self) == True:
            riduzione = irap_lorda * 1.5 / 100
        #Calcolo l'IRAP netta
        totale_irap = irap_lorda - riduzione
        return totale_irap


def dirittoAgevolazione(self): 
        # Verifica se la divisione ATECO è "A03" e se il numero di dipendenti è maggiore di 15
        if self.divisioneAteco == "A03" and self.numeroDipendenti > 15:
            return True
        else:
            return False
        
#######################################################################################################################################################################

class Comune:
    def __init__(self, nomeComune, provincia, abitanti):
        self.nome = nomeComune
        self.provincia = provincia
        self.abitanti = abitanti
        self.impreseRegistrate = [] #Lista di imprese registrate presso il comune
        self.modelliF24Emessi = [] #Lista dei modelli f24 emessi presso il comune

    #Metodo per registrare l'impresa presso il comune

    def registraImpresa(self, impresa):
        self.impreseRegistrate.append(impresa) #Aggiungo l'impresa alla lista di imprese registrate

    #Metodo per emettere un modello f24 presso il comune

    def emettiModelloF24(self, impresa, data):
        modelloF24 = ModelloF24(impresa, data) #Creo un nuovo modello f24 presso il comune
        self.modelliF24Emessi.append(modelloF24) #Aggiungo il modello f24 alla lista dei modelli f24 emessi

#######################################################################################################################################################################

class ModelloF24:
    #costruttore classe Modello
    def __init__(self, impresa, dataModello):
        self.impresa = impresa 
        self.dataModello = dataModello
        self.importoIrap = impresa.calcolaIrap() 

    # preparaF24: il metodo che prepara ilj modello F24 per l'impresa, utilizzando l'importo dell'IRAP calcolato
    def preparaF24(self):
        return {
            "Codice Fiscale dell'impresa": self.impresa.codiceFiscale,
            "Nome dell'impresa": self.impresa.Denominazione,
            "Ragione Sociale dell'impresa": self.impresa.ragioneSociale,
            "Divisione ATECO dell'impresa": self.impresa.divisioneAteco,
            "Data di costituzione dell'impresa": self.impresa.dataCostituzione,
            "Possesso di certificazioni di qualità": self.impresa.certificazioniQualita,
            "Quota IRAP": self.importoIrap,
            "Data emissione modello": self.dataModello
        }
    
