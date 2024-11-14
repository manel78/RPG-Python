from intro import introduction
from combat import combattre
from exploration import explorer, initialiser_map, deplacer
from sauvegarde import sauvegarder
from quitter import quitter
import random


def menu_principal():
    introduction()
    carte = initialiser_map()  # Initialisation de la carte
    position_joueur = [0, 0]  # Position initiale du joueur sur la carte (0,0)

    princes = ["Prince des Ombres", "Prince des Flammes", "Prince des Glaces"]
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Combattre une menace imminente")
        print("2. Explorer le royaume")
        print("3. Sauvegarder votre progression")
        print("4. Prendre une pause (Quitter)")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            combattre(random.choice(princes))
        elif choix == "2":
            position_joueur = deplacer(carte, position_joueur)  # Déplacement et exploration
        elif choix == "3":
            sauvegarder()
        elif choix == "4":
            quitter()
        else:
            print("\nUne lueur confuse vous entoure... Ce choix n'existe pas.\n")


if __name__ == "__main__":
    menu_principal()
