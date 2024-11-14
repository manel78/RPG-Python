import random

# Création de la carte
def initialiser_map():
    return [
        ["Clairière Brumeuse", "Chutes Cristallines", "Forêt Ancienne"],
        ["Grotte des Murmures", "Arbre Cœur-de-vie", "Lac des Reflets"],
        ["Montagnes de Givre", "Ruines Anciennes", "Temple des Lueurs"]
    ]

def afficher_map(carte, position_joueur):
    print("\nCarte du Royaume Féérique :")
    for i, ligne in enumerate(carte):
        ligne_affichee = ""
        for j, lieu in enumerate(ligne):
            if [i, j] == position_joueur:
                ligne_affichee += " [VOUS] "
            else:
                ligne_affichee += f" {lieu[:10]} "  # Affiche une partie du nom pour lisibilité
        print(ligne_affichee)
    print()

def explorer(position_joueur, carte):
    lieux_decouverts = [
        "un éclat d'un cristal ancien",
        "une feuille imprégnée de mémoire",
        "un chuchotement révélant un danger imminent"
    ]
    lieu = carte[position_joueur[0]][position_joueur[1]]
    indice = random.choice(lieux_decouverts)
    print(f"\nVous explorez {lieu}.")
    print(f"Vous découvrez {indice}.\n")

def deplacer(carte, position_joueur):
    afficher_map(carte, position_joueur)
    directions = {
        "n": (-1, 0),
        "s": (1, 0),
        "e": (0, 1),
        "o": (0, -1)
    }
    print("Vous pouvez vous déplacer :")
    print("n - Nord, s - Sud, e - Est, o - Ouest")
    choix = input("Choisissez une direction : ").strip().lower()

    if choix in directions:
        nouvelle_position = [
            position_joueur[0] + directions[choix][0],
            position_joueur[1] + directions[choix][1]
        ]
        # Vérification des limites de la carte
        if 0 <= nouvelle_position[0] < len(carte) and 0 <= nouvelle_position[1] < len(carte[0]):
            position_joueur = nouvelle_position
            explorer(position_joueur, carte)
        else:
            print("\nVous vous heurtez à une barrière invisible. Vous ne pouvez pas aller dans cette direction.\n")
    else:
        print("\nDirection invalide. Essayez de nouveau.\n")

    return position_joueur

