#<>
#Import
from os import system, name
from Fonction_pendu import *
from random import *
import time

class bcolors: #class pour la couleur du texte
    VERT = '\033[92m' 
    JAUNE = '\033[93m' 
    ROUGE = '\033[91m' 
    RESET = '\033[0m' 

#genration de tout les mots
fichier = open("ListeMotsPendu.txt")
mots = []
for ligne in fichier:

    ligne = ligne.rstrip()
    lecture = ligne.split(" ")
    mots = mots+lecture
    
fichier.close()

#generation du mot de la partie
rnd = randint(0,800)
mot = mots[rnd]




#def
def clear():#pour clear le terminal

    if name == 'nt':

        _ = system('cls')

#pour tester la lettre

def test(lettre,mot):

    lst = []
    for i in range(len(mot)):

        if lettre == mot[i]:

            lst.append(i)

    if len(lst) > 0 :

        return 2 , lst

    return 1 , lst #a ajouter a tab
    
#pour def ------
def def_motc(mot):

    motf = ""

    for i in range(len(mot)):

        motf += "-"

    return motf

#pour transformer les ------ en ---A-c
def replace(lst,lettre,motc):

    final_string=""

    for i in range(len(lst)):

        if i >= 1 :

            motc = final_string
            final_string = ""

        for k in range(len(motc)):

            if k == lst[i]:

                final_string += lettre

            else:

                final_string += motc[k]

    return final_string

#def des variables 
res = 0 #juste pour le menu avec while
tab = 0 #le nombre de lettre fausses
motc = def_motc(mot) #motc = ------ (motcaché)
lst = [] #lettre deja utilisé
info = 0 #si la lettre est sorti
print(bcolors.VERT)
print(bcolors.RESET)
clear()


###########################################debut de l'affichage ##########################################################
print(bcolors.JAUNE, " ")

print('''
=============================================================================================================
Valentin MOUCHES                                              
0!/02/2022                              pendu game in python
                                        
                                        for vscode create anotherdirectory
                                        to open  listeMots.txt
=============================================================================================================
''')
print(bcolors.RESET, " ")

#########################################debut du code ###########################################################

while res==0:
    
    info = 0
    time.sleep(1)
    clear() #clear du terminal + affichage de ---- + affichage des lettre deja utilisé + input de la lettre
    print('''
    
    
    ''')
    print( motc)
    print(dessinPendu(tab))

    if len(lst) >= 1:

        print(bcolors.JAUNE)
        print("tu as déja proposé ces lettres", lst , bcolors.RESET)
    

    lettre  = input("entre la lettre : \n").upper()
    if len(lettre) > 1:
        print(bcolors.JAUNE,"il y a plus qu'une lettre dans : ", lettre)
        print("on annule ce tour", bcolors.RESET)

        info = 1

    if lettre == " " or lettre =="":

        info = 1

    if lettre in lst:

        info = 1
    
    #calcul de  teste
    res_test, i = test(lettre,mot)

    

    #si la lettre est fausses : tab augmente + lst ajoute la lettre fausses + affichage d'information 
    if res_test == 1 :

        print(bcolors.ROUGE,"la lettre est fausse ", bcolors.RESET)

        if info == 0:

            tab += 1
            lst.append(lettre)

    #si la lettre est bonne : on remplace les ------ t affiche l'information 
    elif res_test == 2:

        print(bcolors.VERT,"la lettre est bonne", bcolors.RESET)
        motc = replace(i,lettre,motc)

    #fin ? on cherche a savoir esque la partie est fini 
    compte = motc.count("-") #compte le nombre de ---- 

    if tab == 9: #si nb erreur lettre est = a 6 alors la parti se fini

        print(bcolors.VERT,'''┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼''',bcolors.RESET)
        print("tu n'as pas trouvé le mot.Le mot était", mot)
        break

    if compte == 0: #si il y a plus de ---- alors le mots
        
        time.sleep(1)
        clear()
        print('''
    


    ''')
        print( motc)
        print(dessinPendu(tab))

        print()
        print()
        print()
        print()
        print("bravo, tu as trouvé le mot", mot)
        break
        


#</>
print(bcolors.JAUNE,'''
=============================================================================================================
Valentin MOUCHES                                              
0!/02/2022                              pendu game in python
                                        
                                        for vscode create anotherdirectory
                                        to open  listeMots.txt
=============================================================================================================
''', bcolors.RESET)
time.sleep(3)

























