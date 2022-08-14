from random import randint
from time import sleep
from os import system, name
def joueur_d(i):
    if int(i%2) == 0:
        
        return 1
    else:
        
        return 2

def clear():#pour clear le terminal

    if name == 'nt':

        _ = system('cls')

def pause():#pour la pause

    if name == 'nt':

        _ = system('pause')

balle = randint(1,6)

for i in range(6):
    joueur = joueur_d(i)
    sleep(1)

    clear()
    print(f"au joueur {joueur} d'appuyer")
    pause()
    clear()
    if i+1 == balle:
        print(f"joueur {joueur} est mort")
        sleep(1)
        break

    else :
        print(f"la balle n'est pas sortie")
    
sleep(1)
clear()