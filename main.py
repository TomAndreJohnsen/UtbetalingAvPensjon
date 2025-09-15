import kalkulator.beregning as beregning
from kalkulator.sparing import sluttverdi_ved_start
from kalkulator.parametere import Parametere
from kalkulator.parametere import RenteScenario


param = Parametere()

slutt = sluttverdi_ved_start(param)
print("Fondets verdi ved start av pensjon:", round(slutt, 2))
formueskatt = beregning.beregn_formueskatt(param, round(slutt, 2))
print(round(formueskatt, 2))