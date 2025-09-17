# -----------------------------
# GUI
# -----------------------------

import kalkulator.beregning as beregning
from kalkulator.sparing import sluttverdi_ved_start
from kalkulator.parametere import Parametere

formueskatt_list = []


param = Parametere()
slutt, formueskatt_list = sluttverdi_ved_start(param)

formueskatt_totalt = sum(formueskatt_list)
print("Fondets verdi ved start av pensjon: ", f"{round(slutt, 2):,}".replace(",", "."))
print("Total av formueskatt: ", f"{round(formueskatt_totalt, 2):,}".replace(",", "."))
