from setup import Setup
from setup_manager import SetupManager
import csv

# 1️⃣ Créer le manager
manager = SetupManager()

# 2️⃣ Créer quelques setups
setup1 = Setup(
    nom="Setup1",
    hauteur_caisse=120,
    camber=-2,
    caster=5,
    pression_pneus=1.8,
    aero=200,
    poids=250,
    barre_antiroulis_av=30,
    barre_antiroulis_ar=25,
    ackerman=50,
    bv_compression=5,
    bv_detente=7,
    hv_compression=6,
    hv_detente=8,
    ressort_av=400,
    ressort_ar=350,
    epreuve="Autocross",
    terrain="Lisse",
    tarmac="Asphalte",
    meteo="Sec"
)

setup2 = Setup(
    nom="Setup2",
    hauteur_caisse=125,
    camber=-1.5,
    caster=4,
    pression_pneus=1.9,
    aero=210,
    poids=255,
    barre_antiroulis_av=32,
    barre_antiroulis_ar=28,
    ackerman=48,
    bv_compression=6,
    bv_detente=8,
    hv_compression=7,
    hv_detente=9,
    ressort_av=420,
    ressort_ar=360,
    epreuve="Endurance",
    terrain="Accidenté",
    tarmac="Béton",
    meteo="Pluie"
)

# 3️⃣ Ajouter les setups
manager.ajouter_setup(setup1)
manager.ajouter_setup(setup2)

# 4️⃣ Afficher tous les setups
print(manager)

# 5️⃣ Modifier un setup
manager.modifier_setup("Setup1", {"hauteur_caisse": 130, "camber": -1.8})
print(manager)

# 6️⃣ Supprimer un setup
manager.supprimer_setup("Setup2")
print(manager)

# 7️⃣ Sauvegarder dans un fichier
manager.sauvegarde_fichier("test_setups.csv")
# 8️⃣ Lire depuis un fichier
manager2 = SetupManager()
manager2.lecture_fichier("test_setups.csv")
print(manager2)

