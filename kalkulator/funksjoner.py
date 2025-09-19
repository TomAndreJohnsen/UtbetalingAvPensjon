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
    return str(verdi) if verdi is not None else ""

def input_int(prompt, felt):
    while True:
        try:
            value = int(input(prompt))
            setattr(param, felt, value)  # setter verdien direkte i param
            break
        except ValueError:
            print("Ugyldig input. Skriv et heltall.")

def input_date(prompt, attr):
    today = date.today()
    min_alder = 13
    max_alder = 99
    while True:
        try:
            year = int(input("År (YYYY): "))
            alder = today.year - year
            if alder < min_alder or alder > max_alder:
                raise ValueError(f"Alder må være mellom {min_alder} og {max_alder} år.")
            
            month = int(input("Måned (1-12): "))
            day = int(input("Dag (1-31): "))
            value = date(year, month, day)
            setattr(param.person, attr, value)
            break
        except ValueError as e:
            print("Vennligst bruk tall")

# -----------------------------
# Terminal Meny
# -----------------------------
def vis_meny(param):
    clear()
    print("=== Pensjonskalkulator ===\n")

    # Dynamiske verdier (input)
    fodselsdato = vis_verdi(param.person.fodselsdato)
    alder = vis_verdi(getattr(param.person, "alder", ""))
    onsket_netto = vis_verdi(param.uttak.maanedlig_netto)
    start_pensjon = vis_verdi(param.person.pensjon_start)
    slutt_pensjon = vis_verdi(param.person.pensjon_slutt)
    gjeld = vis_verdi(param.person.gjeld)
    eiendom = vis_verdi(param.person.eiendom)
    startkapital = vis_verdi(param.fond.startkapital)
    maaned_innskudd = vis_verdi(param.fond.maanedlig_innskudd)

    # Statisk info (høyre side)
    gevinstskatt = param.skatt.gevinst
    formue_kommune = param.skatt.formue_kommune
    formue_stat_lav = param.skatt.formue_stat_lav
    formue_stat_hoy = param.skatt.formue_stat_hoy
    bunnfradrag = param.skatt.formue_bunnfradrag
    hoy_grense = param.skatt.formue_grense_hoy

    # Print med fast bredde
    print(f"{'Fødselsdato:':<18}{fodselsdato:>10}    {'Gevinstskatt:':<18}{gevinstskatt:<10}")
    print(f"{'Alder:':<18}{alder:>10}    {'Formue kommune:':<18}{formue_kommune:<10}")
    print(f"{'Ønsket netto:':<18}{onsket_netto:>10}    {'Formue stat lav:':<18}{formue_stat_lav:<10}")
    print(f"{'Start pensjon:':<18}{start_pensjon:>10}    {'Formue stat høy:':<18}{formue_stat_hoy:<10}")
    print(f"{'Slutt pensjon:':<18}{slutt_pensjon:>10}    {'Bunnfradrag:':<18}{bunnfradrag:<10}")
    print(f"{'Gjeld:':<18}{gjeld:>10}    {'Høy grense:':<18}{hoy_grense:<10}")
    print(f"{'Eiendom:':<18}{eiendom:>10}")
    print(f"{'Startkapital:':<18}{startkapital:>10}")
    print(f"{'Månedlig innskudd:':<18}{maaned_innskudd:>10}")
    print("\n" + "-"*50 + "\n")