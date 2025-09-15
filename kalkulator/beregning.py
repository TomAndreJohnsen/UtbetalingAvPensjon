#Felles funksjoner som datoer, konvertering osv.
from .parametere import Parametere
from datetime import date
from .sparing import sluttverdi_ved_start

def beregn_formueskatt(param, saldo):
    param: Parametere = Parametere()
    if saldo <= param.bunnfradrag_formue:
        return 0
    
    skattepliktig = saldo - param.bunnfradrag_formue

    skatt = min(skattepliktig, 20_700_000) * param.formueskatt_stat.lav
    if skattepliktig > 20_700_000:
        # HUSK at param.formueskatt_stat.høy er statisk og ikke dynamisk
        skatt += (skattepliktig - 20_700_000) * param.formueskatt_stat.hoy
    
    skatt += skattepliktig * param.formueskatt_kommune

    return skatt
    
