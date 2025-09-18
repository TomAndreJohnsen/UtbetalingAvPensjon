# -----------------------------
# Generelle funksjoner
# -----------------------------
import os
from datetime import date
from kalkulator.parametere import Parametere

param = Parametere

# Brukes for å cleare terminalen for Windows, MacOS og Linux
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Viser tom streng istede for None
def vis_verdi(verdi):
    return '' if verdi is None else verdi

def hent_aar(prompt="Skriv inn år (YYYY): "):
    while True:
        aar_str = input(prompt)
        if not aar_str.isdigit():
            print("Ugyldig input: Kun hele årstall")
            continue
        
        aar = int(aar_str)
        if aar < 1900 or aar > date.today().year:
            print(f"Ugyldig input: Året må være mellom 1900 og {date.today().year}")
            continue
        
        return aar

def hent_maaned(prompt="Skriv inn måned (1-12): "):
    while True:
        try:
            maaned = int(input(prompt))
            if maaned < 1 or maaned > 12:
                raise ValueError("Maaneden må være mellom 1 og 12.")
            return maaned
        except ValueError as e:
            print("Ugyldig input:", e)

def hent_dag(aar, maaned, prompt="Skriv inn dag: "):
    while True:
        try:
            dag = int(input(prompt))
            # prøver å lage en dato for å sjekke om dagen er gyldig
            _ = date(aar, maaned, dag)
            return dag
        except ValueError:
            print("Ugyldig dag for den valgte måneden og året. Prøv igjen.")

# -----------------------------
# Terminal Meny
# -----------------------------
def vis_meny(param):
    clear()
    print("=== Pensjonskalkulator av Tom André ===\n")
    
    # Dynamiske verdier
    print(f"Fødselsdato:          {vis_verdi(param.person.fodselsdato)}")
    print(f"Alder:                {vis_verdi(getattr(param.person, 'alder', ''))}")
    print(f"Ønsket netto pensjon: {vis_verdi(param.uttak.maanedlig_netto)}")
    print(f"Start pensjon:        {vis_verdi(param.person.pensjon_start)}")
    print(f"Slutt pensjon:        {vis_verdi(param.person.pensjon_slutt)}")
    print(f"Gjeld:                {vis_verdi(param.person.gjeld)}")
    print(f"Eiendom:              {vis_verdi(param.person.eiendom)}")
    print(f"Startkapital:         {vis_verdi(param.fond.startkapital)}")
    print(f"Månedlig innskudd:    {vis_verdi(param.fond.maanedlig_innskudd)}\n")
    
    # Statisk info
    print("--- Statisk info ---")
    print(f"Gevinstskatt:         {vis_verdi(param.skatt.gevinst)}")
    print(f"Formue kommune:       {vis_verdi(param.skatt.formue_kommune)}")
    print(f"Formue stat lav:      {vis_verdi(param.skatt.formue_stat_lav)}")
    print(f"Formue stat høy:      {vis_verdi(param.skatt.formue_stat_hoy)}")
    print(f"Bunnfradrag:          {vis_verdi(param.skatt.formue_bunnfradrag)}")
    print(f"Høy grense:           {vis_verdi(param.skatt.formue_grense_hoy)}\n")
    
    print("------------------------\n")