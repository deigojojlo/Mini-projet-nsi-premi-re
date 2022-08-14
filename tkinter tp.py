from tkinter import *

pion = []
def pointeur(event) :
    global pion
    coords = "(" + str(event.x) + ", " + str(event.y) + ")"
    x = event.x
    y = event.y
    chaine.configure(text = "clic gauche en " + coords )
    x1 = x //40
    y1 = y //40
    x2 = 20
    y2 = 20
    x = x1 * 40 + x2
    y = y1 * 40 + y2
    pion.append((can.create_oval(x,y,x,y, outline = 'red', width = 10),x,y))
    chaine1.config(text =f"cercle créé en {x}, {y}")
    print(pion)

    return pion

def supr(event):
    global pion
    if len(pion) >= 1:
        x = pion[0][1]
        y = pion[0][2]
        can.create_oval(x,y,x,y, outline = '#E2E2E2', width = 10)
        can.config()
        del pion[0]
    return pion

fen = Tk()
fen.config(background = '#E2E2E2')
can = Canvas(fen,width = 400, height = 400, bg = '#E2E2E2', bd = 0)
can.bind("<Button-1>", pointeur)
can.bind('<Button-3>', supr )
can.pack()
for i in range(40,400,40):
    can.create_line(i,0,i,400, fill = 'black')
    can.create_line(0,i,400,i, fill = 'black')
    can.config()


chaine = Label(fen, bg = '#E2E2E2')
chaine1 = Label(fen, bg = '#E2E2E2')
chaine.pack()
chaine1.pack()
fen.mainloop()

#####
from tkinter import *

def pointeur(event) :
    global cercle1
    coords = "(" + str(event.x) + ", " + str(event.y) + ")"
    x = event.x
    y = event.y
    chaine.configure(text = "clic gauche en " + coords )
    x = x //40
    y = y //40
    x = x * 40
    y = y * 40
    cercle1 = can.create_oval(x,y,x+40,y+40, fill = 'red')
    chaine1.config(text =f"cercle créé en {x}, {y}")
    can.bind("<Button-1>", supr)
    return cercle1

def supr(event):
    global cercle1
    coords = "(" + str(event.x) + ", " + str(event.y) + ")"
    x = event.x
    y = event.y
    chaine.configure(text = "clic gauche en " + coords )
    x = x //40
    y = y //40
    x = x * 40
    y = y * 40
    can.coords(cercle1, x,y,x+40,y+40)

fen = Tk()
fen.config(background = '#E2E2E2')
can = Canvas(fen,width = 400, height = 400, bg = '#E2E2E2', bd = 0)
can.bind("<Button-1>", pointeur)

can.pack()
for i in range(40,400,40):
    can.create_line(i,0,i,400, fill = 'black')
    can.create_line(0,i,400,i, fill = 'black')
    can.config()


chaine = Label(fen, bg = '#E2E2E2')
chaine1 = Label(fen, bg = '#E2E2E2')
chaine.pack()
chaine1.pack()
fen.mainloop()
###
from tkinter import *

fen = Tk()
fr = Frame(fen)
fen.geometry("300x400")
btn1 = Button(fr,text = "haut", command = lambda : deplace(1))
btn2 = Button(fr,text = "bas", command = lambda : deplace(2))
btn3 = Button(fr,text = "droite", command = lambda : deplace(3))
btn4 = Button(fr,text = "gauche", command = lambda : deplace(4))
btn1.grid(row = 0, column = 0)
btn2.grid(row = 2, column = 0)
btn3.grid(row = 1, column = 1)
btn4.grid(row = 1, column = 0)
fr.pack()


can = Canvas(fen,width = 200, height = 200)
cercle1 = can.create_oval(80,80,120,120, fill = 'black')
can.pack()
co = [80,80,120,120]
def deplace(arg):
    global cercle1
    if arg == 1:
        co[1] -= 2
        co[3] -= 2
    if arg == 2:
        co[1] += 2
        co[3] += 2
    if arg == 3:
        co[0] += 2
        co[2] += 2
    if arg == 4:
        co[0] -= 2
        co[2] -= 2

    can.coords(cercle1,co[0],co[1],co[2],co[3])
    can.config()
    return co
fen.mainloop()
###
from tkinter import *
from time import sleep
fen = Tk()
fr = Frame(fen)
fen.geometry("300x400")
btn1 = Button(fr,text = "haut", command = lambda : deplace(1))
btn2 = Button(fr,text = "bas", command = lambda : deplace(2))
btn3 = Button(fr,text = "droite", command = lambda : deplace(3))
btn4 = Button(fr,text = "gauche", command = lambda : deplace(4))
btn1.grid(row = 0, column = 0)
btn2.grid(row = 2, column = 0)
btn3.grid(row = 1, column = 1)
btn4.grid(row = 1, column = 0)
fr.pack()


can = Canvas(fen,width = 200, height = 200)
cercle1 = can.create_oval(80,80,120,120, fill = 'black')
can.pack()
co = [80,80,120,120]
def deplace(arg):

    global cercle1
    for i in range(10):
        if arg == 1:
            co[1] -= 1
            co[3] -= 1
        if arg == 2:
            co[1] += 1
            co[3] += 1
        if arg == 3:
            co[0] += 1
            co[2] += 1
        if arg == 4:
            co[0] -= 1
            co[2] -= 1

        can.coords(cercle1,co[0],co[1],co[2],co[3])
        can.config()
        sleep(0.1)
        can.update_idletasks()
    return co
fen.mainloop()
###6

from tkinter import *

def clavier(event) :
    global texte, chaine
    texte = texte + event.char
    chaine.configure(text = texte)

texte = ""
fen = Tk()
fen.geometry("150x100")
fen.bind("<Key>", clavier)
chaine = Label(fen)
chaine.pack()
fen.mainloop()
###7
from tkinter import *
fen = Tk()
can = Canvas(fen,width = 200, height = 200)
can.pack()
cercle1 = can.create_oval(80,80,120,120,fill='black')
can.config()
def change_rose(event):
    global cercle1

    cercle1 = can.create_oval(80,80,120,120,fill='pink')
    can.config()
    return cercle1

def change_bleu(event):
    global cercle1
    cercle1 =  can.create_oval(80,80,120,120,fill='blue')
    can.config()
    return cercle1

fen.bind("<KeyPress-r>", change_rose)
fen.bind("<KeyRelease-r>", change_bleu)
fen.mainloop()
###
from tkinter import *
from time import sleep
fen = Tk()
can = Canvas(fen,width = 200, height = 200)
can.pack()
cercle1 = can.create_oval(80,80,120,120,fill='black')
co = [80,80,120,120]
can.config()

def forward(event):
    global co
    for i in range(10):
        co[1] -= 1
        co[3] -= 1
        can.coords(cercle1,co[0],co[1],co[2],co[3])
        can.config()
        can.update_idletasks()
    return co

def back(event):
    global co
    for i in range(10):
        co[1] += 1
        co[3] += 1
        can.coords(cercle1,co[0],co[1],co[2],co[3])
        can.config()
        can.update_idletasks()
    return co

def left(event):
    global co
    for i in range(10):
        co[0] -= 1
        co[2] -= 1
        can.coords(cercle1,co[0],co[1],co[2],co[3])
        can.config()
        can.update_idletasks()
    return co

def right(event):
    global co
    for i in range(10):
        co[0] += 1
        co[2] += 1
        can.coords(cercle1,co[0],co[1],co[2],co[3])
        can.config()

        can.update_idletasks()
    return co
fen.bind("<KeyPress-Left>", left)
fen.bind("<KeyRelease-Right>",right)
fen.bind("<KeyPress-Up>", forward)
fen.bind("<KeyPress-Down>",back)

fen.mainloop()


######
from tkinter import *
import random

joueur = 1

# Create window
root = Tk()
root.geometry("500x500")
root.minsize(width = 350, height = 400)

label_puiss = Label(root,text = "Puissance 4", font=("calibri", 20), bd = 0)
label_puiss.pack()
label_j = Label(root, text = "", bd = 0, font= ("calibri",15))
label_j.pack()
Canvas_img = Canvas(width= 350, height=300, bg="blue")
Canvas_img.pack(pady = 20)


for i in range(50,350,50):
    ligne = Canvas_img.create_line(i,0,i,350)
    ligne = Canvas_img.create_line(0,i,350,i)
for x in  range(0,350,50):
    for y in range(0,300,50):
        Canvas_img.create_oval(x,y,x+50,y+50, width= 1, fill="white")


def win_condition(tab:list,joueur:int):
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
            if lsttest3 == [joueur,joueur,joueur,joueur]:
                return True
    return False




def diagonale_g_d(tab:list,joueur:int):
    lst_test = []
    for x in range(3):
        for y in range(4):
            lst_test = []
            for i in range(4):
                lst_test.append(tab[x+i][y+i])
            if lst_test == [joueur,joueur,joueur,joueur]:
                return True
    return False

def init_puissance4():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
tab = init_puissance4()


compteur = -1
def def_compteur(compteur):

    compteur += 1
    return compteur

def def_joueur(compteur):
    if compteur % 2 == 0:
        return 1
    else:
        return 2



def joue_pion(joueur: int, colonne: int):
    # Trouve la ligne à remplir
    for i in range(5, -1, -1):
        if tab[i][colonne] == 0:
            tab[i][colonne] = joueur
            return tab,i




def place(event):
    global tab
    global compteur
    global joueur
    colonne = event.x
    colonne = (colonne//50)
    print(colonne)
    label_j.config(text = "au joueur " + str(joueur) + " de jouer")
    compteur = def_compteur(compteur)
    joueur = def_joueur(compteur)
    if tab[0][colonne] != 0:
            pass
    else:
        tab,ligne = joue_pion(joueur , colonne)
        update(joueur,colonne,ligne)
        info = win_condition(tab,joueur)
        if info == True:
            label_j.config(text = "le joueur " + str(joueur) + " a gagné")

        return tab

def update(joueur, colonne, ligne):
    if joueur == 1:
        Canvas_img.create_oval(colonne * 50,ligne*50,colonne*50+50,ligne*50+50, width= 1, fill="red")
    if joueur == 2:
        Canvas_img.create_oval(colonne * 50,ligne*50,colonne*50+50,ligne*50+50, fill="yellow")
    Canvas_img.config()


root.bind('<Button-1>', place)

root.mainloop()
