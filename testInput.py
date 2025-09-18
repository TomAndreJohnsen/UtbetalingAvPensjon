# test_input.py
from datetime import date
from kalkulator.parametere import Parametere
from kalkulator.funksjoner import hent_aar, hent_maaned, hent_dag, clear, vis_meny

param = Parametere()

def input_int(prompt, felt):
    while True:
        try:
            value = int(input(prompt))
            setattr(param, felt, value)  # setter verdien direkte i param
            break
        except ValueError:
            print("Ugyldig input. Skriv et heltall.")

def input_date(prompt, attr):
    while True:
        try:
            year = int(input("År (YYYY): "))
            month = int(input("Måned (1-12): "))
            day = int(input("Dag (1-31): "))
            value = date(year, month, day)
            setattr(param.person, attr, value)
            break
        except ValueError as e:
            print("Ugyldig dato:", e)

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

