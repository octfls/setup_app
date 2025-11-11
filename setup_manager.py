#Fichier pour gerer les setups
import csv
from setup import Setup

class SetupManager:
    def __init__(self):
        self.setups = []
    
    def __str__(self):
        return "\n".join([str(s) for s in self.setups])
    
    def ajouter_setup(self, x):    #Ici x est un objet de la classe setup
        self.setups.append(x)
    
    def supprimer_setup(self, nom):
        for elt in self.setups:
            if elt.nom == nom:
                self.setups.remove(elt)
                return "Suppression effectuée"
        return "Le setup que vous voulez supprimer n'existe pas"

    def modifier_setup(self, nom, dico):
        for elt in self.setups:
            if elt.nom == nom:
                for para, valeur in dico.items():
                    if hasattr(elt, para) and getattr(elt, para) != valeur:
                        setattr(elt, para, valeur)
                return "Modification effectuée"
        return "Le setup que vous voulez modifier n'existe pas"

    def lecture_fichier(self, fichier="setups.csv"):
        with open(fichier, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                # ici tu peux convertir les colonnes numériques si nécessaire
                current_setup = Setup(*row)
                self.setups.append(current_setup)



    def sauvegarde_fichier(self, fichier="setups.csv"):
        with open(fichier, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for s in self.setups:
                writer.writerow([
                    s.nom, s.hauteur_caisse, s.camber, s.caster, s.pression_pneus, s.aero, s.poids,
                    s.barre_antiroulis_av, s.barre_antiroulis_ar, s.ackerman,
                    s.bv_compression, s.bv_detente,
                    s.hv_compression, s.hv_detente,
                    s.ressort_av, s.ressort_ar,
                    s.epreuve, s.terrain, s.tarmac, s.meteo
                ])



