
#def
def clear():
    print("\n"* 100)

def init_puissance_4():
    lst = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    return lst

def affichage(tab):
    for i in range(len(tab)):
        print(tab[i])

def joueur_un(ligne,colonne,tab):
    tab[ligne][colonne] = 1
    return tab

def joueur_deux(ligne,colonne,tab):
    tab[ligne][colonne] = 2
    return tab

def joue_pion(joueur,colonne,tab):
    for i in range(5,-1,-1):
            if tab[i][colonne] == 0:
                ligne = i
                if joueur == 1:
                    new_tab = joueur_un(ligne,colonne,tab)   #revoie vers la fct joueur_x qui modifie la ligne et la colonne
                    return new_tab
                elif joueur == 2 :
                    new_tab = joueur_deux(ligne,colonne,tab)
                    return new_tab


def win_condition(tab,joueur):
    infoh = horizontale(tab,joueur)
    infov = verticale(tab,joueur)
    infodgd = diagonale_g_d(tab,joueur)
    infoddg = diagonale_d_g(tab,joueur)
    lst = [infoh ,infov ,infodgd , infoddg]
    return True in lst

def horizontale(tab,joueur):
    for i in range(6):
        for k in range(3):
            if tab[i][k:k+4] == [joueur,joueur,joueur,joueur]:
                return True

def verticale(tab, joueur):
    for i in range(3):
        for k in range(7):
            lst_test = []
            for j in range(4):
                lst_test.append(tab[i+j][k])
            if lst_test == [joueur,joueur,joueur,joueur]:
                return True


def diagonale_d_g(tab,joueur):

    lst_test = []

    for i in range(4):
        for n in range(4,7):
            lsttest3 = []
            for m in range (4):
                lsttest3.append(tab[i+m-1][n-m-1])#notre relation de coordonée est (x,y) (x-3,y+3)
            if lst_test == [joueur,joueur,joueur,joueur]: #le test
                return True

    return False

def diagonale_g_d(tab,joueur):

    lst_test = []

    for x in range(4):

        for y in range(4,7):

            lst_test = []
            for i in range(4):

                    lst_test.append(tab[x+i-1][y-i-1])  #notre relation de coordonée est (x,y) (x-3,y+3)
            if lst_test == [joueur,joueur,joueur,joueur]: #le test

                return True

    return False

#value
tab = init_puissance_4()
boucle = 1
nb_tour = 1

#menu
while boucle != 0:
    print("colonne:")
    print([1, 2, 3, 4, 5, 6, 7])
    print()
    print(affichage(tab))
    if nb_tour % 2 == 0:
        joueur = 2
    if nb_tour % 2 != 0:
        joueur = 1
    print(f"au joueur {joueur} de jouer")
    action = int(input("entre la colonne dans laquel tu veux placer ton pion : \n ")) -1
    clear()
    tab = joue_pion(joueur,action,tab)
    test = win_condition(tab,joueur)
    if test == True:
        print(f"joueur {joueur} a gagné")
        print(affichage(tab))
        break
    print("colonne:")
    print([1, 2, 3, 4, 5, 6, 7])
    print()
    print(affichage(tab))
    clear()
    nb_tour += 1
    if 0 in tab == False:
        print("match nul")
        break