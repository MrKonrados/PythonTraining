"""
GOAL

Write a simple game that allows the user and the computer to take turns selecting moves to use against each other. 
Both the computer and the player should start out at the same amount of health (such as 100), and should be able to 
choose between the three moves:

    1.  The first move should do moderate damage and has a small range (such as 18-25).
    2.  The second move should have a large range of damage and can deal high or low damage (such as 10-35).
    3.  The third move should heal whoever casts it a moderate amount, similar to the first move.

After each move, a message should be printed out that tells the user what just happened, and how much health the user 
and computer have. Once the user or the computer's health reaches 0, the game should end.

SUBGOALS

    1.  When someone is defeated, make sure the game prints out that their health has reached 0, and nota negative 
        number.
    2.  When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
    3.  Give each move a name.
"""
import random

MENU = """1 - Średni atak [18-25]
2 - Potężny atak [10-35]
3 - Leczenie [18-25]
0 - Koniec gry"""

human_health = npc_health = 100


def moderate_attack():
    hit = random.randint(18, 25)
    print('Słaby atak [{}]'.format(hit))
    return hit


def strong_attack():
    hit = random.randint(10, 35)
    print('Mocny atak [{}]'.format(hit))
    return hit


def heal():
    heal = random.randint(18, 25)
    print('Leczenie [{}]'.format(heal))
    return heal


is_human_move = random.choice([True, False])
while human_health > 0 and npc_health > 0:
    if is_human_move:
        is_human_move = False
        try:
            print("Ty: {}, Przeciwnik: {}".format(human_health, npc_health))
            print(MENU)
            action = int(input("Wybierz: "))
        except ValueError:
            print("\nBłąd! Wybrana akcja musi być cyfrą!\n")
            is_human_move = True
            continue

        if action == 1:
            npc_health -= moderate_attack()
        elif action == 2:
            npc_health -= strong_attack()
        elif action == 3:
            human_health += heal()
            if human_health > 100:
                human_health = 100
        elif action == 0:
            print('\nWyjście')
            break
        else:
            print("\nBłąd! Wybierz cyfre ponownie\n")
            is_human_move = True;
    else:
        is_human_move = True
        print("\nTura przeciwnika...")
        if npc_health == 100:
            human_health -= random.choice([strong_attack, moderate_attack])()
        elif npc_health > 35:
            action = random.choice([strong_attack, moderate_attack, heal])
            if action == heal:
                npc_health += action()
                if npc_health > 100:
                    npc_health = 100
            else:
                human_health -= action()
        else:
            c = random.choice([1, 2, 3])
            if c < 3:
                npc_health += heal()
            else:
                human_health -= random.choice([strong_attack, moderate_attack])()
        print("---")

if human_health > 0:
    print("\n---\nWygrałeś :-)\n---\n")
else:
    print("\n---\nPrzegrałeś :-(\n---\n")
