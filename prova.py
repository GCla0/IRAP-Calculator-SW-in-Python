
from time import strptime
from datetime import date, datetime


def main ():
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
    #return data
if __name__ == "__main__":
    main() 