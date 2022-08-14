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


lst = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nb_mine = randint(0,25)
mine = lst[nb_mine]
test = []
i = 0
while i != -1:
    clear()
    
    print("ces lettres on deja été joué")
    print(test)
    joueur = joueur_d(i)
    print(f"au joueur {joueur} de jouer")
    demine = input("entre une lettre : \n")
    sleep(1)
    clear()
    joueur = joueur_d(i)
    if demine in test:
        
        pass
    
        
    elif demine in lst:
        if demine == mine :
            print(f"joueur {joueur} a perdu")
            sleep(1)
         
            break
        else :
            test.append(demine)
            i += 1
    else :
        pass
sleep(1)
clear()

