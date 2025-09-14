from datetime import date

class Parametere:
    def __init__(self):
        #Persondata
        self.fodselsdato = date(1987, 4, 3)
        self.pensjon_start = date(2054, 4, 3)
        self.pensjon_slutt = date(2080, 4, 3)

        #Fond
        self.startkapital_brutto = 0
        self.maanedlig_innskudd = 2000
        self.rente_fond = RenteScenario(lav=0.075, mid=0.1039, hoy=0.1524)
        self.inflasjon = 0.025
        self.rente_kostnad = 0.002

        #Uttak
        self.uttak_per_maaned_netto = 48000
        self.uttak_per_maaned_brutto = self.beregn_brutto_fra_netto(self.uttak_per_maaned_netto)

        #Skatt
        self.skatt_gevinst = 0.3784
        self.formueskatt_kommune = 0.00525
        self.formueskatt_stat = RenteScenario(lav=0.00475, hoy=0.00575)

        #Formue
        self.gjeld = 0
        self.formue_eiendom = 0
        

    def beregn_brutto_fra_netto(self, netto):
        return netto / (1 - self.skatt_gevinst)

    