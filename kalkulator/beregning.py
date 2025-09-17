#Felles funksjoner som datoer, konvertering osv.
from .parametere import Parametere
from datetime import date
from .sparing import sluttverdi_ved_start

def beregn_formueskatt(param, saldo):
    param: Parametere = Parametere()
    if saldo <= param.skatt.formue_bunnfradrag:
        return 0
    
    skattepliktig = saldo - param.skatt.formue_bunnfradrag

    skatt = min(skattepliktig, 20_700_000) * param.skatt.formue_stat_lav
    if skattepliktig > 20_700_000:
        # HUSK at param.formueskatt_stat.høy er statisk og ikke dynamisk
        skatt += (skattepliktig - 20_700_000) * param.skatt.formue_stat_hoy
    
    skatt += skattepliktig * param.skatt.formue_kommune

    return skatt
    
