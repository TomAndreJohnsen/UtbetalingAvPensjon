#Alt som gjelder innskudd og vekst før pensjon
from .parametere import Parametere
from datetime import date


def maanedlig_saldo(startbelop, maander, aarlig_rente, maanedlig_uttak):
    saldo_liste = []
    saldo = startbelop
    for mnd in range(maander):
        saldo += saldo * (aarlig_rente/12)
        saldo -= maanedlig_uttak
        saldo_liste.append(saldo)
    return saldo_liste


def sluttverdi_ved_start(param):
    param: Parametere = Parametere()
    maaneder = (param.pensjon_start.year - param.fodselsdato.year) * 12 + \
           (param.pensjon_start.month - param.fodselsdato.month)
    saldo = param.startkapital_brutto
    for _ in range(maaneder):
        saldo = saldo * (1 + param.rente_fond.mid / 12) + param.maanedlig_innskudd
    return saldo

