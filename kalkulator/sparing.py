#Alt som gjelder innskudd og vekst før pensjon

def maanedlig_saldo(startbelop, maander, aarlig_rente, maanedlig_uttak):
    saldo_liste = []
    saldo = startbelop
    for mnd in range(maander):
        saldo += saldo * (aarlig_rente/12)
        saldo -= maanedlig_uttak
        saldo_liste.append(saldo)
    return saldo_liste


