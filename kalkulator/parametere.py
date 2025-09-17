import datetime as dt
from dataclasses import dataclass, field

# -----------------------------
# Funksjoner
# -----------------------------
def hent_verdi(input, default):
    return input if input is not None else default

def beregn_brutto_fra_netto(netto, gevinst):
    return netto / (1 - gevinst) 

# -----------------------------
# Default verdier
# -----------------------------
default_fodselsdato = dt.date(1987, 4, 3)
default_pensjon_start = dt.date(2054, 4, 3)
default_pensjon_slutt = dt.date(2080, 4, 3)
default_person_gjeld = 0
default_person_eiendom = 0

default_skatt_gevinst = 0.3784
default_formue_kommune = 0.007
default_formue_stat_lav = 0.00475
default_formue_stat_hoy = 0.00575
default_formue_bunnfradrag = 1_760_000
default_formue_grense_hoy = 20_000_000

default_startkapital = 10_000_000
default_maanedlig_innskudd = 2000
default_rente_lav = 0.075
default_rente_mid = 0.1039
default_rente_hoy = 0.1524
default_inflasjon = 0.025
default_kostnad = 0.002

default_maanedlig_netto = 35000

# -----------------------------
# Dataclasses
# -----------------------------
@dataclass
class Person:
    fodselsdato: dt.date = default_fodselsdato
    pensjon_start: dt.date = default_pensjon_start
    pensjon_slutt: dt.date = default_pensjon_slutt
    gjeld: int = default_person_gjeld
    eiendom: int = default_person_eiendom

@dataclass
class Skatt:
    gevinst: float = default_skatt_gevinst
    formue_kommune: float = default_formue_kommune
    formue_stat_lav: float = default_formue_stat_lav
    formue_stat_hoy: float = default_formue_stat_hoy
    formue_bunnfradrag: float = default_formue_bunnfradrag
    formue_grense_hoy: int = default_formue_grense_hoy

@dataclass
class Fond:
    startkapital: int = default_startkapital
    maanedlig_innskudd: int = default_maanedlig_innskudd
    rente_lav: float = default_rente_lav
    rente_mid: float = default_rente_mid
    rente_hoy: float = default_rente_hoy
    inflasjon: float = default_inflasjon
    kostnad: float = default_kostnad

@dataclass
class Uttak:
    maanedlig_netto: int = default_maanedlig_netto
    maanedlig_brutto: int = field(default_factory=lambda: beregn_brutto_fra_netto(default_maanedlig_netto, default_skatt_gevinst))

@dataclass
class Parametere:
    person: Person = field(default_factory=Person)
    skatt: Skatt = field(default_factory=Skatt)
    fond: Fond = field(default_factory=Fond)
    uttak: Uttak = field(default_factory=Uttak)

# Entry verdier
entry_fodselsdato = None
entry_pensjon_start = None
entry_pensjon_slutt = None
entry_person_gjeld = None
entry_person_eiendom = None

entry_skatt_gevinst = None
entry_formue_kommune = None
entry_formue_stat_lav = None
entry_formue_stat_hoy = None
entry_formue_bunnfradrag = None
entry_formue_grense_hoy = None

entry_startkapital = None
entry_maanedlig_innskudd = None
entry_rente_lav = None
entry_rente_mid = None
entry_rente_hoy = None
entry_inflasjon = None
entry_kostnad = None

entry_maanedlig_netto = None

# Input verdier
input_fodselsdato = hent_verdi(entry_fodselsdato, default_fodselsdato)
input_pensjon_start = hent_verdi(entry_pensjon_start, default_pensjon_start)
input_pensjon_slutt = hent_verdi(entry_pensjon_slutt, default_pensjon_slutt)
input_person_gjeld = hent_verdi(entry_person_gjeld, default_person_gjeld)
input_person_eiendom = hent_verdi(entry_person_eiendom, default_person_eiendom)

input_skatt_gevinst = hent_verdi(entry_skatt_gevinst, default_skatt_gevinst)
input_formue_kommune = hent_verdi(entry_formue_kommune, default_formue_kommune)
input_formue_stat_lav = hent_verdi(entry_formue_stat_lav, default_formue_stat_lav)
input_formue_stat_hoy = hent_verdi(entry_formue_stat_hoy, default_formue_stat_hoy)
input_formue_bunnfradrag = hent_verdi(entry_formue_bunnfradrag, default_formue_bunnfradrag)
input_formue_grense_hoy = hent_verdi(entry_formue_grense_hoy, default_formue_grense_hoy)

input_startkapital = hent_verdi(entry_startkapital, default_startkapital)
input_maanedlig_innskudd = hent_verdi(entry_maanedlig_innskudd, default_maanedlig_innskudd)
input_rente_lav = hent_verdi(entry_rente_lav, default_rente_lav)
input_rente_mid = hent_verdi(entry_rente_mid, default_rente_mid)
input_rente_hoy = hent_verdi(entry_rente_hoy, default_rente_hoy)
input_inflasjon = hent_verdi(entry_inflasjon, default_inflasjon)
input_kostnad = hent_verdi(entry_kostnad, default_kostnad)

input_maanedlig_netto = hent_verdi(entry_maanedlig_netto, default_maanedlig_netto)


param = Parametere(
    person=Person(
        fodselsdato = input_fodselsdato,
        pensjon_start = input_pensjon_start,
        pensjon_slutt = input_pensjon_slutt,
        gjeld = input_person_gjeld,
        eiendom = input_person_eiendom
    ),
    skatt=Skatt(
        gevinst = input_skatt_gevinst,
        formue_kommune = input_formue_kommune,
        formue_stat_lav = input_formue_stat_lav,
        formue_stat_hoy = input_formue_stat_hoy,
        formue_bunnfradrag = input_formue_bunnfradrag,
        formue_grense_hoy = input_formue_grense_hoy
    ),
    fond=Fond(
        startkapital = input_startkapital,
        maanedlig_innskudd = input_maanedlig_innskudd,
        rente_lav = input_rente_lav,
        rente_mid = input_rente_mid,
        rente_hoy = input_rente_hoy,
        inflasjon = input_inflasjon,
        kostnad = input_kostnad
    ),
    uttak=Uttak(
        maanedlig_netto = input_maanedlig_netto,
        maanedlig_brutto = beregn_brutto_fra_netto(input_maanedlig_netto, input_skatt_gevinst)
    )
)
