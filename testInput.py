# test_input.py
from datetime import date
from kalkulator.parametere import Parametere
from kalkulator.funksjoner import clear, vis_meny, input_int, input_date

param = Parametere()

def main():
    while True:
        clear()
        vis_meny(param)  # alltid vis meny på toppen

        print("Velg hva du vil fylle inn:")
        print("1 - Fødselsdato")
        print("2 - Ønsket netto pensjon")
        print("3 - Start pensjon")
        print("4 - Slutt pensjon")
        print("5 - Gjeld")
        print("6 - Eiendom")
        print("7 - Startkapital")
        print("8 - Månedlig innskudd")
        print("0 - Avslutt")
        valg = input("Ditt valg: ")

        if valg == "1":
            input_date("Fødselsdato", "fodselsdato")
        elif valg == "2":
            param.uttak.maanedlig_netto = int(input("Ønsket netto pensjon: "))
        elif valg == "3":
            input_date("Start pensjon", "pensjon_start")
        elif valg == "4":
            input_date("Slutt pensjon", "pensjon_slutt")
        elif valg == "5":
            param.person.gjeld = int(input("Gjeld: "))
        elif valg == "6":
            param.person.eiendom = int(input("Eiendom: "))
        elif valg == "7":
            param.fond.startkapital = int(input("Startkapital: "))
        elif valg == "8":
            param.fond.maanedlig_innskudd = int(input("Månedlig innskudd: "))
        elif valg == "0":
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    main()

