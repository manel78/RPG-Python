import random
import time

def combattre(prince):
    attaques = ["Lancer de Lueurs", "Éclat Enflammé", "Sceau d'Épines", "Onde de Protection"]
    print(f"\nUn {prince} apparaît, ses yeux brûlant de convoitise pour le pouvoir d'Eloria !")
    print("Vous brandissez votre pouvoir magique.")
    while True:
        choix_attaque = random.choice(attaques)
        degats = random.randint(5, 20)
        print(f"Vous utilisez {choix_attaque} et infligez {degats} points de dégâts au {prince} !")
        if degats > 15:
            print(f"Le {prince} recule, terrifié par la puissance que vous déployez. Vous avez triomphé !\n")
            break
        else:
            print(f"Le {prince} riposte mais votre lumière vacillante tient bon.\n")
            time.sleep(1)
