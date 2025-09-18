# test_input.py
import os
from datetime import date
from kalkulator.parametere import Parametere

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

param = Parametere()

clear()
print("Hei og velkommen til min Pensjonkalkulator")
print("Først må du fylle ut litt informasjon")
input("Press Enter for å gå videre")

year = int(input("Hvilket år er du født?: "))
month = int(input("Måned: "))
day = int(input("Dag :"))

fodseldato = date(year, month, day)

param.person.fodselsdato = fodseldato
print("Fødselsdato satt til :", param.person.fodselsdato)