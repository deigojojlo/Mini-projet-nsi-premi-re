from tkinter import *

#def de nos variable 
tab = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
compteur = 0
inf_deja_win = 0
joueur = 1

#def def def de calcul
def update(arg:str,x,y):
    global compteur
    global tabb
    global inf_deja_win
    compteur = def_compteur(compteur)
    joueur = def_joueur(compteur)
    
    if joueur == 2:
        color = 'red'
        texte = "X"
    else:
        color = 'yellow'
        texte = "O"
    tab[x][y] = color
    wintest =win(tab,color)
    if inf_deja_win == 1:
        pass
    elif wintest == True:
        print("win")
        exec(f"{arg} = Button(frame_jeu, width=10, height= 5, fg ='black', bg = color,text = texte, font=('calibri', 10))")
        label_inf.config(text = f"le joueur {joueur} a gagné")
        exec(f"{arg}.grid(row = x, column = y)")  
        inf_deja_win = 1
    else:
        exec(f"{arg} = Button(frame_jeu, text = texte, width=10, height= 5, fg ='black', bg = color, font=('calibri',10))")
        label_inf.config(text= f"au joueur {joueur} de jouer")
        exec(f"{arg}.grid(row = x, column = y)")
    frame_jeu.config()


def reset():
    global tabb
    global tab
    global inf_deja_win
    global compteur 
    compteur = 0
    for i in range(3):
        for k in range(3):
            tab[i][k] = 0
    tabb = def_tabb()
    inf_deja_win = 0
    print(tab)
    return inf_deja_win, tab, tabb, compteur


def def_compteur(compteur):
    return compteur + 1


def def_joueur(compteur):
    if compteur% 2 == 0:
        return 1
    else:
        return 2

def win(tab,color):
    wint = []
    wint.append(h(tab,color))
    wint.append(v(tab,color))
    wint.append(dd(tab,color))
    wint.append(dg(tab,color))
    return True in wint


def h(tab,color):
    for i in range(3):
        if tab[i] == [color,color,color]:
            return True
    return False


def v(tab,color):
    for i in range(3):
        lst = []
        for k in range(3):
            lst.append(tab[k][i])
        if lst == [color,color,color]:
            return True
    return False
            

def dd(tab,color):
    lst = []
    lst.append(tab[0][0])
    lst.append(tab[1][1])
    lst.append(tab[2][2])
    if lst == [color,color,color]:
        return True
    return False


def dg(tab,color):
    lst = []
    lst.append(tab[0][2])
    lst.append(tab[1][1])
    lst.append(tab[2][0])
    if lst == [color,color,color]:
        return True
    return False


def def_tabb():
    tabb = [
        [],
        [],
        []
    ]
    nw = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("nw",0,0))
    tabb[0].append(nw)
    n = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("n",0,1))
    tabb[0].append(n)
    ne = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("ne",0,2))
    tabb[0].append(ne)
    mw = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("n",1,0))
    tabb[1].append(mw)
    m = Button(frame_jeu, width=10, height= 5,  bg = "white",text = "",command= lambda : update("n",1,1))
    tabb[1].append(m)
    me = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("n",1,2))
    tabb[1].append(me)
    sw = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("n",2,0))
    tabb[2].append(sw)
    s = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("n",2,1))
    tabb[2].append(s)
    se = Button(frame_jeu, width=10, height= 5, bg = "white",text = "", command= lambda : update("n",2,2))
    tabb[2].append(se)

    nw.grid(row=0, column=0)
    n.grid(row=0, column=1)
    ne.grid(row=0,column=2)
    mw.grid(row=1,column= 0)
    m.grid(row= 1, column= 1)
    me.grid(row= 1, column= 2)
    se.grid(row=2, column=2)
    s.grid(row = 2, column= 1)
    sw.grid(row = 2, column= 0)
    return tabb

#def de la fenetre
fen = Tk()
fen.geometry("500x500")
fen.minsize(500,500)
frame_jeu = Frame(fen)
label_inf = Label(fen,text = f"au joueur {joueur} de jouer", font = ("calibri",15))
label_titre = Label(fen, text = f"Morpion", font = ("calibri",20))
btn_reset = Button(fen, text= "reset", width= 10, command= reset)
btn_reset.pack(side= TOP, anchor=SE)
label_titre.pack()
label_inf.pack(pady = 10)

#creation de notre tab de boutons
tabb = def_tabb()

#affichage
frame_jeu.pack()

#lancement de la fenetre
fen.mainloop()