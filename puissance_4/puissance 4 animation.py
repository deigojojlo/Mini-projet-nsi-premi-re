from tkinter import *
from time import sleep
from random import randint

#def des variables a prédefinir
a = "Ⓙ"
b = "Ⓡ"
compteur = 0 #permet de calcul le nombre de coups deja jouer et donc le a qui de jouer
tab = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]
width = 60 #largeur et hauteur des canvas
height = 60


#IA bot
def calcul_intelligent(tab):
    for i in range(3):  #parcoure
        for k in range(7):#le tableau
            lst_test = [] #init notre list test
            for j in range(4): #créé notre list de len 4
                lst_test.append((tab[i+j][k],i+j,k))
            testcg = 0
            testcag = 0
            replace = []
            for h in range(4):
                if lst_test[h][0] == "Ⓡ":
                    testcg += 1
                elif lst_test[h][0] == "Ⓙ":
                    testcag += 1
                elif lst_test[h][0] == 0:
                    replace.append((lst_test[h][1],lst_test[h][2]))
            if (testcg == 3 or testcag == 3) and len(replace) >= 1:
                a = replace[0][1]
                x_bot = replace[0][0]
                y_bot = replace[0][1]
                if i == 5:
                    return  x_bot,y_bot
                if tab[replace[0][0]+1][a]  != 0 :
                    return  x_bot,y_bot
    for i in range(6):
        for k in range(4):
            lst_test= []

            for j in range(4):
              lst_test.append((tab[i][k+j],i,k+j))
            testcg = 0
            testcag = 0
            replace = []
            for h in range(4):
                if lst_test[h][0] == "Ⓡ":
                    testcg += 1
                elif lst_test[h][0] == "Ⓙ":
                    testcag += 1
                elif lst_test[h][0] == 0:
                    replace.append((lst_test[h][1],lst_test[h][2]))

            if (testcg == 3 or testcag == 3) and len(replace) >= 1:
                a = replace[0][1]
                x_bot = replace[0][0]
                y_bot = replace[0][1]
                if i == 5:
                    return  x_bot,y_bot
                if tab[replace[0][0]+1][a]  != 0 :
                    return  x_bot,y_bot


    for x in range(3):
        for y in range(3,6):
            lst_test = []
            for i in range (4):
                lst_test.append((tab[x+i][y-i],x+i,y-i))
            testcg = 0
            testcag = 0
            replace = []
            for h in range(4):
                if lst_test[h][0] == "Ⓡ":
                    testcg += 1
                elif lst_test[h][0] == "Ⓙ":
                    testcag += 1
                elif lst_test[h][0] == 0:
                    replace.append((lst_test[h][1],lst_test[h][2]))
            if (testcg == 3 or testcag == 3) and len(replace) >= 1:
                a = replace[0][1]
                x_bot = replace[0][0]
                y_bot = replace[0][1]
                if i == 5:
                    return  x_bot,y_bot
                if tab[replace[0][0]+1][a]  != 0 :
                    return  x_bot,y_bot
    for x in range(3):
        for y in range(4):
            lst_test = []
            for i in range(4):
                lst_test.append((tab[x+i][y+i],x+i,y+i))
            testcg = 0
            testcag = 0
            replace = []
            for h in range(4):
                if lst_test[h][0] == "Ⓡ":
                    testcg += 1
                elif lst_test[h][0] == "Ⓙ":
                    testcag += 1
                elif lst_test[h][0] == 0:
                    replace.append((lst_test[h][1],lst_test[h][2]))
            if (testcg == 3 or testcag == 3) and len(replace) >= 1:
                a = replace[0][1]
                x_bot = replace[0][0]
                y_bot = replace[0][1]
                if i == 5:
                    return  x_bot,y_bot
                if tab[replace[0][0]+1][a]  != 0 :
                    return  x_bot,y_bot



def init_bot(tab):
    try :
        x,y = calcul_intelligent(tab)
        tab = joueur_deux(x,y,tab)
        print("a")
        return tab
    except TypeError:
        tab = coup_bot(tab)
        return tab



#pb calcul pas si la colonne est pleinne
def coup_bot(tab:list):
    m = 0
    while m == 0:
        colonne = randint(0,6) #créer une action
        for i in range(5,-1,-1):#cherche a quelle ligne il faut placer le pion
            if tab[i][colonne] == 0:
                ligne = i
                new_tab = joueur_deux(ligne,colonne,tab) #créer le new_tab avec l'action du bot
                return new_tab




def def_compteur(): #calcul du nombre de coup deja jouer
    global compteur
    compteur += 1
    return compteur




def joueur_un(ligne:int,colonne:int,tab:list): #action de placer 1
    global a
    tab[ligne][colonne] = a
    return tab




def joueur_deux(ligne:int,colonne:int,tab:list): #action de placer 2
    global b
    tab[ligne][colonne] = b
    return tab




def joue_pion(joueur:int,colonne:int,tab:list): #action de dire où placer
        for i in range(5,-1,-1):
            if tab[i][colonne] == 0:
                ligne = i
                if joueur == 1:
                    new_tab = joueur_un(ligne,colonne,tab)
                    return new_tab
                elif joueur == 2 :
                    new_tab = init_bot(tab)
                    return new_tab
        return False




def win_condition(tab:list,joueur:int):
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




def horizontale(tab:list,joueur:int):
    for i in range(6):
        for k in range(3):
            if tab[i][k:k+4] == [joueur,joueur,joueur,joueur]:
                return True




def verticale(tab:list, joueur:int):
    for i in range(3):
        for k in range(7):
            lst_test = []
            for j in range(4):
                lst_test.append(tab[i+j][k])
            if lst_test == [joueur,joueur,joueur,joueur]:
                return True




def diagonale_d_g(tab:list,joueur:int):

    for x in range(3):
        for y in range(3,6):
            lsttest3 = []
            for i in range (4):
                lsttest3.append(tab[x+i][y-i])
            if lsttest3 == [joueur,joueur,joueur,joueur]: #le test
                return True
    return False




def diagonale_g_d(tab:list,joueur:int):
    lst_test = []
    for x in range(3):
        for y in range(4):
            lst_test = []
            for i in range(4):
                lst_test.append(tab[x+i][y+i])  #notre relation de coordonée est (x,y) (x-3,y+3)
            if lst_test == [joueur,joueur,joueur,joueur]: #le test
                return True
    return False




def q_joueur(compteur):
    if compteur % 2 == 0:
        joueur = 1
    if compteur % 2 != 0:
        joueur = 2

    return joueur




def colonne(arg:int):
    global tab

    for i in range(2):
        tabl = joue_pion(i+1,arg-1,tab)
        if tabl != False:
            if i == 0:
                actualise_tab(tabl,1,i)
                update(tabl)
            elif i == 1:
                actualise_tab(tabl,2,i)
                update(tabl)




def actualise_tab(tab:list,joueur:int,i:int):
    label_soustitre.config(text=f"au joueur 1(jaune) de jouer")
    info = win_condition(tab,joueur)
    if info == True :
        if i == 0:
            label_fin.pack()
        elif i == 1:
            label_finb.pack()
        running = False




def def_joueur():
    global compteur
    if compteur % 2 == 0:
        joueur = 2
    elif compteur % 2 != 0:
        joueur = 1
    return joueur




def update(tabl:list):
    global image
    global image1
    global image2
    global lst
    global width, height
    for i in range(6):#actualisation des 42 images
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
fenetre.geometry("720x650") #taille
fenetre.minsize(700,400) #taille min
fenetre.iconbitmap("C:/Users/valentinmouches/desktop/puissance_4/logo.ico") #icone de la fenetre
fenetre.config(background="#D2D2D2") #couleur arriere plan

#def des frames
frame = Frame(fenetre, bg='#D2D2D2')
frame_button = Frame(fenetre, bg="#D2D2D2")
frame_jeu = Frame(fenetre)
frame_img = Frame(fenetre)

#affiche puissance 4(le nom du jeu)
label_titre = Label(frame,text="Puissance 4", font=("calibri", 40),bg="#D2D2D2" )
label_j = Label(frame,text="partie contre un bot",font=("calibri, 20"), bg="#D2D2D2")
#affiche qui doit jouer
label_soustitre = Label(frame,text=f"au joueur 1 (jaune) de jouer", font=("calibri", 20),bg="#D2D2D2" )
#affiche la fin de la partie/vainqueur/ match nul
label_fin = Label(fenetre,text=f"joueur 1 a gagné", font=("calibri", 20), bg = "#D2D2D2")
label_finb = Label(fenetre,text=f"le bot a gagné", font=("calibri", 20), bg = "#D2D2D2")
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

#importation des images
image =PhotoImage(file="C:/Users/valentinmouches/desktop/puissance_4/capture-min.png")
image1 = PhotoImage(file="C:/Users/valentinmouches/desktop/puissance_4/capture_r_min.png")
image2 = PhotoImage(file="C:/Users/valentinmouches/desktop/puissance_4/capture_j_min.png")


#creation de 42 image  palcer dans une grille
for i in range(6):
    for k in range(7):
        exec(f"canvas{i}{k} = Canvas(frame_img, width = {width}, height = {height}, bg=\"blue\", bd=0, highlightthickness = 0)")
        exec(f"canvas{i}{k}.create_image({width}/2, {height} /2,image = image)")
        exec(f"canvas{i}{k}.grid(row = {i} , column = {k})")

def restart():
    global tab
    tab = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    update(tab)
    return tab

#pack/affichage de tout les elements
bouton = Button(fenetre,text="exit",command = fenetre.destroy, height= 1,width = 10,font=("calibri",9) )
bouton.pack(side = TOP, anchor= NE)
boutonreset = Button(fenetre,text="reset",command = restart, height= 1,width = 10,font=("calibri",9) )
boutonreset.pack(side = TOP, anchor= SE)

label_titre.pack()
label_j.pack()
label_soustitre.pack()
frame.pack()
frame_button.pack(pady = 25)
frame_img.pack()

#affichage de la fenetre
fenetre.mainloop()
#'''
#valentin Mouchès
#'''