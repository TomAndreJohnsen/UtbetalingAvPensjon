# -----------------------------
# Alt av verdier og data
# -----------------------------

import datetime as dt
from dataclasses import dataclass, field

# -----------------------------
# Funksjoner
# -----------------------------
def beregn_brutto_fra_netto(netto, gevinst):
    return netto / (1 - gevinst) 


# -----------------------------
# Dataclass
# -----------------------------

@dataclass
class Person:
    fodselsdato: dt.date | None = None
    pensjon_start: dt.date = dt.date(2054, 4, 3)
    pensjon_slutt: dt.date = dt.date(2080, 4, 3)
    gjeld: int = 0
    eiendom: int = 0

@dataclass
class Skatt:
    gevinst: float = 0.3784
    formue_kommune: float = 0.007
    formue_stat_lav: float = 0.00475
    formue_stat_hoy: float = 0.00575
    formue_bunnfradrag: float = 1_760_000
    formue_grense_hoy: int = 20_000_000

@dataclass
class Fond:
    startkapital: int = 0
    maanedlig_innskudd: int = 0
    rente_lav: float = 0.075
    rente_mid: float = 0.1039
    rente_hoy: float = 0.1524
    inflasjon: float = 0.025
    kostnad: float = 0.002

@dataclass
class Uttak:
    maanedlig_netto: int = 0
    maanedlig_brutto: float = field(default_factory=lambda: beregn_brutto_fra_netto(35_000, 0.3784))

@dataclass
class Parametere:
    person: Person = field(default_factory=Person)
    skatt: Skatt = field(default_factory=Skatt)
    fond: Fond = field(default_factory=Fond)
    uttak: Uttak = field(default_factory=Uttak)