#Felles funksjoner som datoer, konvertering osv.
from .parametere import Parametere

def beregn_formueskatt(param, saldo):
    param: Parametere = Parametere()
    formue = saldo + param.formue_eiendom - param.gjeld
    # Husk at param.formueskatt_stat.hoy er satt statisk å må endres til valg
    skatt = formue * (param.formueskatt_kommune + param.formueskatt_stat.hoy)
    return max(skatt, 0)

