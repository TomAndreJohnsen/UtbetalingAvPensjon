#Felles funksjoner som datoer, konvertering osv.
from .parametere import Parametere

def beregn_formueskatt(param, saldo):
    param: Parametere = Parametere()
    formue = saldo + param.formue_eiendom - param.gjeld
    skatt = formue * (param.formueskatt_kommune + param.formueskatt_stat.hoy)
    return max(skatt, 0)