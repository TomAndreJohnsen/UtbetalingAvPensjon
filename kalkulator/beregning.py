# -----------------------------
# Felles funksjoner som datoer, konvertering osv.
# -----------------------------

from .parametere import Parametere
from datetime import date
from .sparing import sluttverdi_ved_start


def beregn_formueskatt(param, saldo):
    if saldo <= param.skatt.formue_bunnfradrag:
        return 0
    
    skattepliktig = saldo - param.skatt.formue_bunnfradrag

    skatt = min(skattepliktig, 20_700_000) * param.skatt.formue_stat_lav
    if skattepliktig > 20_700_000:
        skatt += (skattepliktig - 20_700_000) * param.skatt.formue_stat_hoy
    
    skatt += skattepliktig * param.skatt.formue_kommune

    return skatt
