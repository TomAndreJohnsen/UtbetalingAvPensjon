#Alt som gjelder innskudd og vekst før pensjon
from .parametere import Parametere
from datetime import date, timedelta


def maanedlig_saldo(startbelop, maander, aarlig_rente, maanedlig_uttak):
    saldo_liste = []
    saldo = startbelop
    for mnd in range(maander):
        saldo += saldo * (aarlig_rente/12)
        saldo -= maanedlig_uttak
        saldo_liste.append(saldo)
    return saldo_liste

def neste_maaned(dato):
    if dato.month == 12:
        return date(dato.year + 1, 1, dato.day)
    else:
        return date(dato.year, dato.month + 1, dato.day)

def sluttverdi_ved_start(param):
    from kalkulator.beregning import beregn_formueskatt
    param: Parametere = Parametere()
    saldo = param.startkapital_brutto
    dato = date.today()

    while dato < param.pensjon_start:
        # HUSK param.rente_fond.mid er statisk å må endres
        saldo = saldo * (1 + param.rente_fond.mid / 12) + param.maanedlig_innskudd
        dato = neste_maaned(dato)

        if dato.month == 12:
            skatt = beregn_formueskatt(param, saldo)
            saldo -= skatt

    return saldo