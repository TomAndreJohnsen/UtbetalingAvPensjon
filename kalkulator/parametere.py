# -----------------------------
# Alt av verdier og data
# -----------------------------

from datetime import date
from dataclasses import dataclass, field

# -----------------------------
# Funksjoner
# -----------------------------

def beregn_brutto_fra_netto(netto: float, gevinst: float) -> float:
    """Beregner brutto fra netto og gevinstskatt."""
    return netto / (1 - gevinst)

# -----------------------------
# Dataclasses
# -----------------------------

@dataclass
class Person:
    fodselsdato: date | None = None
    pensjon_start: date | None = None 
    pensjon_slutt: date | None = None
    gjeld: int | None = None
    eiendom: int | None = None

    @property
    def alder(self) -> str | int:
        if self.fodselsdato is None:
            return ""
        today = date.today()
        return today.year - self.fodselsdato.year - (
            (today.month, today.day) < (self.fodselsdato.month, self.fodselsdato.day)
        )

@dataclass
class Skatt:
    gevinst: float = 0.3784
    formue_kommune: float = 0.007
    formue_stat_lav: float = 0.00475
    formue_stat_hoy: float = 0.00575
    formue_bunnfradrag: int = 1_760_000
    formue_grense_hoy: int = 20_000_000

@dataclass
class Fond:
    startkapital: int | None = None
    maanedlig_innskudd: int | None = None
    rente_lav: float = 0.075
    rente_mid: float = 0.1039
    rente_hoy: float = 0.1524
    inflasjon: float = 0.025
    kostnad: float = 0.002

@dataclass
class Uttak:
    maanedlig_netto: int | None = None
    maanedlig_brutto: float = field(
        default_factory=lambda: beregn_brutto_fra_netto(35_000, 0.3784)
    )

@dataclass
class Parametere:
    person: Person = field(default_factory=Person)
    skatt: Skatt = field(default_factory=Skatt)
    fond: Fond = field(default_factory=Fond)
    uttak: Uttak = field(default_factory=Uttak)