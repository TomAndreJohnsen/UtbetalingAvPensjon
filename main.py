from kalkulator.pensjon import maanedlig_saldo

STARTBELOP = 1_000_000
MAANEDER = 120
AARLIG_RENTE = 0.075
MAANEDLIG_UTTAK = 10_000
INFLASJON = 0.025
FONDSKOST = 0.002

resultat = maanedlig_saldo(STARTBELOP, MAANEDER, AARLIG_RENTE, MAANEDLIG_UTTAK)
print("Sluttbalanse:", resultat[-1])