from tkinter import *
import time
from random import randint
import os



a = "Ⓙ"
b = "Ⓡ"
compteur = 0
tab = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

lst = [[],[],[],[],[],[]]
for i in range(6):
    for k in range(7):
        lst[i].append(f"canvas{i}{k}")





def def_compteur():

    global compteur
    compteur += 1
    return compteur

def joueur_un(ligne,colonne,tab):

    global a
    tab[ligne][colonne] = a
    return tab

def joueur_deux(ligne,colonne,tab):

    global b
    tab[ligne][colonne] = b
    return tab

def joue_pion(joueur,colonne,tab):

        for i in range(5,-1,-1):

            if tab[i][colonne] == 0:

                ligne = i

                if joueur == 1:

                    new_tab = joueur_un(ligne,colonne,tab)
                    return new_tab

                elif joueur == 2 :

                    new_tab = joueur_deux(ligne,colonne,tab)
                    return new_tab
        return False


def win_condition(tab,joueur):


    if joueur == 1:

        joueur = "Ⓙ"

    elif joueur == 2:

        joueur = "Ⓡ"

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
    for x in range(4):
        for y in range(4,7):
            lsttest3 = []
            for i in range (4):
                lsttest3.append(tab[x+i-1][y-i-1])#notre relation de coordonée est (x,y) (x-3,y+3)
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


def q_joueur(compteur):

    if compteur % 2 == 0:

        joueur = 1

    if compteur % 2 != 0:

        joueur = 2

    return joueur
joueur = q_joueur(compteur)

def colonne(arg):
    global tab
    compteur = def_compteur()
    joueur = q_joueur(compteur)


    if arg == 1:
        tabl = joue_pion(joueur,0,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)


    if arg == 2:

        tabl = joue_pion(joueur,1,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)
    if arg == 3:
        tabl = joue_pion(joueur,2,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)
    if arg == 4:
        tabl = joue_pion(joueur,3,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)
    if arg == 5:
        tabl = joue_pion(joueur,4,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)
    if arg == 6:
        tabl = joue_pion(joueur,5,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)
    if arg == 7:
        tabl = joue_pion(joueur,6,tab)
        if tabl != False:

            actualise_tab(tabl,joueur)
            update(tabl)

def actualise_tab(tab,joueur):


    label_soustitre.config(text=f"au joueur {joueur} de jouer")
    info = win_condition(tab,joueur)

    if info == True :

        label_fin.pack()
        label_soustitre.destroy()
        running = False

def def_joueur():

    global compteur

    if compteur % 2 == 0:

        joueur = 2

    elif compteur % 2 != 0:

        joueur = 1

    return joueur




def update(tabl):

    global image
    global image1
    global image2
    global lst
    global wight, height

    for i in range(6):

        for k in range(7):

            if tabl[i][k] == 0:

                exec(f"canvas{i}{k}.create_image({width}/2, {height}/2,image = image)")
                exec(f"canvas{i}{k}.config()")

            elif tabl[i][k] == "Ⓙ":

                exec(f"canvas{i}{k}.create_image({width}/2, {height}/2,image = image2)")
                exec(f"canvas{i}{k}.config()")

            elif tabl[i][k] == "Ⓡ":

                exec(f"canvas{i}{k}.create_image({width}/2, {height}/2,image = image1)")
                exec(f"canvas{i}{k}.config()")

#creation de la fenetre
fenetre = Tk()

fenetre.title("puissance 4") #nom
fenetre.geometry("1080x720") #taille
fenetre.minsize(700,400) #taille min
fenetre.iconbitmap("C:/Users/ValentinMOUCHES/Desktop/puissance_4/logo.ico") #icon de la fenetre
fenetre.config(background="#D2D2D2") #couleur arriere plan

#def des frames
frame = Frame(fenetre, bg='#D2D2D2')
frame_button = Frame(fenetre, bg="#D2D2D2")
frame_jeu = Frame(fenetre)
frame_img = Frame(fenetre)

#affiche puissance 4(le nom du jeu)
label_titre = Label(frame,text="Puissance 4", font=("calibri", 40),bg="#D2D2D2" )
#affiche qui doit jouer
label_soustitre = Label(frame,text=f"au joueur {joueur} de jouer", font=("calibri", 20),bg="#D2D2D2" )
#affiche la fin de la partie/vainqueur/ match nul
label_fin = Label(fenetre,text=f"joueur {joueur} a gagné", font=("calibri", 20), bg = "#D2D2D2")

#def des bouttons de la fenetre
place_button1 = Button(frame_button, text="colonne 1" , font=("calibri",9) , command = lambda : colonne(1))
place_button2 = Button(frame_button, text="colonne 2" , font=("calibri",9) , command = lambda : colonne(2))
place_button3 = Button(frame_button, text="colonne 3" , font=("calibri",9) , command = lambda : colonne(3))
place_button4 = Button(frame_button, text="colonne 4" , font=("calibri",9) , command = lambda : colonne(4))
place_button5 = Button(frame_button, text="colonne 5" , font=("calibri",9) , command = lambda : colonne(5))
place_button6 = Button(frame_button, text="colonne 6" , font=("calibri",9) , command = lambda : colonne(6))
place_button7 = Button(frame_button, text="colonne 7" , font=("calibri",9) , command = lambda : colonne(7))

#def de la grille pour que les bouttons soit cote a cote
place_button1.grid(row = 0 , column = 0)
place_button2.grid(row = 0 , column = 2)
place_button3.grid(row = 0 , column = 4)
place_button4.grid(row = 0 , column = 6)
place_button5.grid(row = 0 , column = 8)
place_button6.grid(row = 0 , column = 10)
place_button7.grid(row = 0 , column = 12)

image =PhotoImage(file="C:/Users/ValentinMOUCHES/Desktop/puissance_4/capture-min.png")
image1 = PhotoImage(file="C:/Users/ValentinMOUCHES/Desktop/puissance_4/capture_r_min.png")
image2 = PhotoImage(file="C:/Users/ValentinMOUCHES/Desktop/puissance_4/capture_j_min.png")

width = 60
height = 60


for i in range(6):

    for k in range(7):

        exec(f"canvas{i}{k} = Canvas(frame_img, width = {width}, height = {height}, bg=\"blue\", bd=0, highlightthickness = 0)")
        exec(f"canvas{i}{k}.create_image({width}/2, {height} /2,image = image)")


for i in range(6):
    for k in range(7):
        exec(f"canvas{i}{k}.grid(row = {i} , column = {k})")

#pack/affichage de tout les elements
label_titre.pack()
label_soustitre.pack()
frame.pack()
frame_button.pack(pady = 25)
frame_img.pack()


#affichage de la fenetre
fenetre.mainloop()

'''
valentin Mouchès
'''