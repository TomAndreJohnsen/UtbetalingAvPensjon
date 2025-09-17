# test_input.py
from datetime import date
from kalkulator.parametere import Parametere, Person, Skatt, Fond, Uttak, beregn_brutto_fra_netto
from kalkulator.sparing import sluttverdi_ved_start

# -----------------------------
# Funksjon for enkel dato-input
# -----------------------------
def les_dato(prompt, default):
    s = input(f"{prompt} (YYYY-MM-DD) [{default}]: ")
    if s.strip() == "":
        return default
    y, m, d = map(int, s.split("-"))
    return date(y, m, d)

def les_float(prompt, default):
    s = input(f"{prompt} [{default}]: ")
    return float(s) if s.strip() != "" else default

def les_int(prompt, default):
    s = input(f"{prompt} [{default}]: ")
    return int(s) if s.strip() != "" else default

# -----------------------------
# Les input fra terminal
# -----------------------------
person_fodselsdato = les_dato("Fødselsdato", date(1987,4,3))
person_pensjon_start = les_dato("Start pensjon", date(2054,4,3))
person_pensjon_slutt = les_dato("Slutt pensjon", date(2080,4,3))
person_gjeld = les_int("Gjeld", 0)
person_eiendom = les_int("Eiendom", 0)

skatt_gevinst = les_float("Skattegevinst", 0.3784)
formue_kommune = les_float("Formueskatt kommune", 0.007)
formue_stat_lav = les_float("Formueskatt stat lav", 0.00475)
formue_stat_hoy = les_float("Formueskatt stat høy", 0.00575)
formue_bunnfradrag = les_int("Formue bunnfradrag", 1_760_000)
formue_grense_hoy = les_int("Formue grense høy", 20_000_000)

fond_startkapital = les_int("Startkapital fond", 10_000_000)
fond_maanedlig_innskudd = les_int("Månedlig innskudd", 2000)
fond_rente_mid = les_float("Rente mid", 0.1039)

uttak_maanedlig_netto = les_int("Månedlig netto uttak", 35_000)

# -----------------------------
# Opprett Parametere
# -----------------------------
param = Parametere(
    person=Person(
        fodselsdato=person_fodselsdato,
        pensjon_start=person_pensjon_start,
        pensjon_slutt=person_pensjon_slutt,
        gjeld=person_gjeld,
        eiendom=person_eiendom
    ),
    skatt=Skatt(
        gevinst=skatt_gevinst,
        formue_kommune=formue_kommune,
        formue_stat_lav=formue_stat_lav,
        formue_stat_hoy=formue_stat_hoy,
        formue_bunnfradrag=formue_bunnfradrag,
        formue_grense_hoy=formue_grense_hoy
    ),
    fond=Fond(
        startkapital=fond_startkapital,
        maanedlig_innskudd=fond_maanedlig_innskudd,
        rente_mid=fond_rente_mid
    ),
    uttak=Uttak(
        maanedlig_netto=uttak_maanedlig_netto,
        maanedlig_brutto=beregn_brutto_fra_netto(uttak_maanedlig_netto, skatt_gevinst)
    )
)

# -----------------------------
# Beregn og vis resultater
# -----------------------------
resultat = sluttverdi_ved_start(param)
if isinstance(resultat, tuple):
    slutt_saldo, formueskatt_list = resultat
else:
    slutt_saldo = resultat
    formueskatt_list = []

print("\nFondets verdi ved start av pensjon:", round(slutt_saldo, 2))
print("Formueskatt per år (bare registrerte år):", formueskatt_list)