#Fichier pour coder la classe setup

class Setup:
    def __init__(self, nom,
                 hauteur_caisse,
                 camber,
                 caster,
                 pression_pneus,
                 aero,
                 poids,
                 barre_antiroulis_av=None,
                 barre_antiroulis_ar=None,
                 ackerman=None,
                 bv_compression=None,
                 bv_detente=None,
                 hv_compression=None,
                 hv_detente=None,
                 ressort_av=None,
                 ressort_ar=None,
                 epreuve=None,
                 terrain=None,
                 tarmac=None,
                 meteo=None):
        self.nom = nom
        self.hauteur_caisse = hauteur_caisse
        self.camber = camber
        self.caster = caster
        self.pression_pneus = pression_pneus
        self.aero = aero
        self.poids = poids
        self.barre_antiroulis_av = barre_antiroulis_av
        self.barre_antiroulis_ar = barre_antiroulis_ar
        self.ackerman = ackerman
        self.bv_compression = bv_compression
        self.bv_detente = bv_detente
        self.hv_compression = hv_compression
        self.hv_detente = hv_detente
        self.ressort_av = ressort_av
        self.ressort_ar = ressort_ar
        self.epreuve = epreuve
        self.terrain = terrain
        self.tarmac = tarmac
        self.meteo = meteo

    def __str__(self):
        return (f"{self.nom} | {self.epreuve} | {self.terrain} | {self.tarmac} | {self.meteo} | "
                f"Hauteur:{self.hauteur_caisse} | Camber:{self.camber} | Caster:{self.caster} | "
                f"Barre AV:{self.barre_antiroulis_av}, AR:{self.barre_antiroulis_ar} | Ackerman:{self.ackerman} | "
                f"BV C:{self.bv_compression}, D:{self.bv_detente} | "
                f"HV C:{self.hv_compression}, D:{self.hv_detente} | "
                f"Ressort AV:{self.ressort_av}, AR:{self.ressort_ar})")
    
    
