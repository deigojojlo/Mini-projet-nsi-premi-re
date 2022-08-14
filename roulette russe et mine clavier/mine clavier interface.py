from tkinter import *
from random import randint
fenetre =Tk()
joueur = 1
clavierl1 = ["a","z","e","r","t","y","u","i","o","p"]
clavierl2 = ["q","s","d","f","g","h","j","k","l","m"]
clavierl3 = ["w","x","c","v","b","n"]
frame1 = Frame(fenetre)
frame2 = Frame(fenetre)
frame3 = Frame(fenetre)
frameh = Frame(fenetre)
frame_test = Frame()
fenetre.title("Mine clavier by FM")
fenetre.geometry("720x500")
fenetre.minsize(720,720)
fenetre.config(background="#D2D2D2")

label_titre = Label(fenetre, text = "Mine Clavier" , bg ="#D2D2D2", font=("calibri", 20), width=25)
label_joueur = Label(fenetre, text=f"au joueur {joueur} de jouer ", bg ="#D2D2D2", font=("calibri", 15), width=25)


def reset():
    global clavierl1, clavierl2, clavierl3
    mine.config()
    compteur = 0
    joueur = 1
    label_joueur.config(text=f"au joueur {joueur} de jouer ")
    for i in range(10):
        lettre = clavierl1[i].upper()
        exec(f"canvas{lettre}.config(bg='#D2D2D2')")
    for i in range(10):
        lettre = clavierl2[i].upper()
        exec(f"canvas{lettre}.config(bg='#D2D2D2')")
    for i in range(6):
        lettre = clavierl3[i].upper()
        exec(f"canvas{lettre}.config(bg='#D2D2D2')")


bouton = Button(fenetre,text = "reset", bg = "#D2D2D2", width=10, command = reset )
bouton.pack(side = TOP, anchor=SE)
label_titre.pack()
label_joueur.pack(pady=20)




A = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/A.png")
canvasA = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasA.create_image(20,20,image = A)
canvasA.grid(row= 0, column = 0)


B = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/B.png")
canvasB = Canvas(frame3,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasB.create_image(20,20,image = B)
canvasB.grid(row= 0, column = 4)

C = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/C.png")
canvasC = Canvas(frame3,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasC.create_image(20,20,image = C)
canvasC.grid(row= 0, column = 2)

D = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/D.png")
canvasD = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasD.create_image(20,20,image = D)
canvasD.grid(row= 0, column = 2)

E = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/E.png")
canvasE = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasE.create_image(20,20,image = E)
canvasE.grid(row= 0, column = 2)

F = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/F.png")
canvasF = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasF.create_image(20,20,image = F)
canvasF.grid(row= 0, column = 3)

G = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/G.png")
canvasG = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasG.create_image(20,20,image = G)
canvasG.grid(row= 0, column = 4)

H = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/H.png")
canvasH = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasH.create_image(20,20,image = H)
canvasH.grid(row= 0, column = 5)

I = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/I.png")
canvasI = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasI.create_image(20,20,image = I)
canvasI.grid(row= 0, column = 7)

J = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/J.png")
canvasJ = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasJ.create_image(20,20,image = J)
canvasJ.grid(row= 0, column = 6)

K = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/K.png")
canvasK = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasK.create_image(20,20,image = K)
canvasK.grid(row= 0, column = 7)

L = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/L.png")
canvasL = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasL.create_image(20,20,image = L)
canvasL.grid(row= 0, column = 8)

M = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/M.png")
canvasM = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasM.create_image(20,20,image = M)
canvasM.grid(row= 0, column = 9)

N = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/N.png")
canvasN = Canvas(frame3,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasN.create_image(20,20,image = N)
canvasN.grid(row= 0, column = 5)

O = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/O.png")
canvasO = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasO.create_image(20,20,image = O)
canvasO.grid(row= 0, column = 8)

P = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/P.png")
canvasP = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasP.create_image(20,20,image = P)
canvasP.grid(row= 0, column = 9)

Q = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/Q.png")
canvasQ = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasQ.create_image(20,20,image = Q)
canvasQ.grid(row= 0, column = 0)

R = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/R.png")
canvasR = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasR.create_image(20,20,image = R)
canvasR.grid(row= 0, column = 3)

S = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/S.png")
canvasS = Canvas(frame2,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasS.create_image(20,20,image = S)
canvasS.grid(row= 0, column = 1)

T = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/T.png")
canvasT = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasT.create_image(20,20,image = T)
canvasT.grid(row= 0, column = 4)

U = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/U.png")
canvasU = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasU.create_image(20,20,image = U)
canvasU.grid(row= 0, column = 6)

V = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/V.png")
canvasV = Canvas(frame3,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasV.create_image(20,20,image = V)
canvasV.grid(row= 0, column = 3,)

W = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/W.png")
canvasW = Canvas(frame3,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasW.create_image(20,20,image = W)
canvasW.grid(row= 0, column = 0)

X = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/X.png")
canvasX = Canvas(frame3,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasX.create_image(20,20,image = X)
canvasX.grid(row= 0, column = 1)

Y = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/Y.png")
canvasY = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasY.create_image(20,20,image = Y)
canvasY.grid(row= 0, column = 5)

Z = PhotoImage(file="c:/users/valentinmouches/desktop/roulette russe/Z.png")
canvasZ = Canvas(frame1,width=40, height=40, bg = "#D2D2D2",bd=0, highlightthickness = 0)
canvasZ.create_image(20,20,image = Z)
canvasZ.grid(row= 0, column = 1)

rmine = randint(0,25)
rmine -= 1
if rmine <10:
    rmine = clavierl1[rmine].upper()
elif 10 <= rmine < 20:
    rmine = clavierl2[rmine-10].upper()
elif rmine >= 20:
    rmine = clavierl3[rmine-20].upper()


lst_inf = []
compteur = 0

def def_joueur(compteur):
    if compteur % 2 == 0:
        joueur = 1
    else:
        joueur = 2
    return joueur

def get_entry(event):
    global clavierl1,clavierl2,clavierl3,compteur
    m = mine.get()
    m = m.upper()
    mine.delete(0,last=len(m))
    if len(m) >= 1:
        if m != rmine:
            if m in lst_inf:
                pass
            else:
                m = m[0]
                exec(f"canvas{m.upper()}.config(bg = 'green')")
                lst_inf.append(m)
                ompteur = def_compteur()
                joueur = def_joueur(compteur)
                label_joueur.config(text = f"au joueur {joueur} de jouer ")
        elif m == rmine:
            m = m[0]
            ompteur = def_compteur()
            joueur = def_joueur(compteur)
            exec(f"canvas{m.upper()}.config(bg = 'red')")
            label_joueur.config(text= f"le joueur {joueur} a gagné")
            mine.destroy()
compteur = 0
def def_compteur():
    global compteur
    compteur += 1 
    return compteur

mine = Entry(fenetre, bd = 10,relief=FLAT, )
fenetre.bind('<Return>', get_entry)



frame1.pack()
frame2.pack()
frame3.pack()
mine.pack(pady= 25)
fenetre.mainloop()
