import kalkulator.beregning as beregning
from kalkulator.sparing import sluttverdi_ved_start
from kalkulator.parametere import Parametere
from kalkulator.parametere import RenteScenario

formueskatt_list = []

param = Parametere()
slutt, formueskatt_list = sluttverdi_ved_start(param)

print("Fondets verdi ved start av pensjon: ", f"{round(slutt, 2):,}".replace(",", "."))
#print(formueskatt_list)
