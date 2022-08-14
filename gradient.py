import abc
from distutils.log import info
from turtle import *
from random import *
import time

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

#######
print(bcolors.OK)
print("__________________________________________________________________________________________________________________________________")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("")
print("                                                             gradient                                                             ")
print("                      .       .                                      ")
print("                             / `.   .' \"                            ")
print("                     .---.  <    > <    >  .---.                     ")
print("                     |    \  \ - ~ ~ - /  /    |                     ")
print("         _____          ..-~             ~-..-~                      ")
print("        |     |   \~~~\.'                    `./~~~/                 ")
print("       ---------   \__/                        \__/                  ")
print("      .'  O    \     /               /       \  \"                   ")
print("     (_____,    `._.'               |         }  \/~~~/              ")
print("      `----.          /       }     |        /    \__/               ")
print("            `-.      |       /      |       /      `. ,~~|           ")
print("                ~-.__|      /_ - ~ ^|      /- _      `..-'           ")
print("                    |     /        |     /     ~-.     `-. _  _  _   ")
print("                     |_____|        |_____|         ~ - . _ _ _ _ _> ")
print("")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("__________________________________________________________________________________________________________________________________")
print(bcolors.RESET)
#######
####test
demi_tour = 3.25
taille = demi_tour * 2
preset_info = 0
preset = ""
avis_preset = ""
exit_preset = 0
preset_info = 0
textef =  []
texte_info = ""
info_grad = ""
texte = ""
pl = 0

#test7
while 1:
    if texte != "":
        break
    if info_grad == "OUI":
        break
    if texte_info == "":

        print("veux-tu afficher un texte ? ")
        print("oui/non \n")
        texte_info = input()
        print()
        print()

    if texte_info.lower() == "oui":

        texte = input("entre le texte a écrire : \n")
        texte = texte.upper()
        nbl = len(texte)
        pl = (nbl*-60)/2
        print()
        print("de qu'elle couleur veux-tu écrire")
        print("rouge/vert/bleu/jaunne/noir/other/... \n")
        couleur_texte = input("")
        print()
        print()




    if info_grad == "":

        print("veux-tu éxécuter un gradiant ? ")
        print("oui/non \n")

        info_grad = input()
        info_grad = info_grad.upper()
        print()

    if info_grad.lower() == "non" and texte_info.lower() == "non":
        break


#test
if info_grad.lower() == "oui":
    while 1:
        #preset
        if exit_preset == 1:
            avis_preset = "non"


        elif preset_info ==1 :

            break
        elif info_grad == "NON":
            break
        elif preset_info != 1 :
            print("veux-tu éxécuter un preset ?")
            print(( "\'oui/non \'"))
            avis_preset = input()
            print()
            print()




        if avis_preset.lower() == "oui":
            while 1:
                print("quelle preset veux-tu éxécuter ? ")
                print("\'rgb/soleil/bj/exit/\'")
                preset = input()
                print()
                if preset == "rgb":

                    (x0,y0,z0) = 255,0,0
                    (x1,y1,z1) = 0,255,0
                    (x2,y2,z2 )= 0,0,255
                    nb_color = 3
                    preset_info = 1
                    delta = 0.01
                    break

                elif preset == "soleil":
                    (x0,y0,z0) = 149,0,255
                    (x1,y1,z1) = 255,65,35
                    (x2,y2,z2 )= 255,149,0

                    nb_color = 3
                    preset_info = 1
                    delta = 0.01

                    break

                elif preset == "bj":

                    (x0,y0,z0) = 34,193,195
                    (x1,y1,z1) = 253,187,45


                    nb_color = 2
                    preset_info = 1
                    delta = 0.005

                    break

                elif preset == "exit":

                    exit_preset = 1
                    break


                else:

                    pass


        elif avis_preset.lower() == "non":

            nb_color = int(input("nombre de couleurs dans le gradiant : \n"))


            delta = 0.005 + 0.005*(nb_color - 2)
            print()

            break

        else :

            break


class vector:

    def __init__(self,x=0,y=0,z=0):

        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vec):

        return vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __radd__(self, vec):

        return self.__add__(vec)

    def __mul__(self, scalar):

        if isinstance(scalar, float) or isinstance(scalar, int):

            return vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):

        return self.__mul__(scalar)

    def __str__(self):

        return f"{self.x},{self.y},{self.z}"

    def __rstr__(self):

        return f"{self.x},{self.y},{self.z}"

    def __repr__(self):

        return repr((self.x, self.y, self.z))

    def toList(self):

        return [self.x, self.y, self.z]

    def ic(self):

        return(vector(int(self.x),int(self.y),int(self.z)))








'''def   alphabet'''

def A() :

    left(70)
    forward(50)
    a = position()
    forward(50)
    right(140)
    forward(100)
    penup()
    setx(a[0])
    sety(a[1])
    pendown()
    left(70)
    forward(35)
    right(90)
    penup()
    forward(45)
    left(90)
    forward(25)
    pendown()
    penup()
    forward(10)
    pendown()


def B() :

    left(90)
    penup()
    forward(10)
    pendown()
    forward(90)
    right(90)
    forward(10)
    for i in range(70):

        right(2.5)
        forward(1)

    left(180)

    for i in range(75):

        right(2.5)
        forward(1)

    forward(10)
    penup()
    left(180)
    forward (30)
    forward(10)
    pendown()

def C(): # revu

    penup()
    forward(70)
    left(180)
    pendown()
    forward(10)

    for i in range(180):

        right(1)
        forward(1)

    penup()
    right(90)
    forward(100)
    left(90)
    forward(10)
    pendown()

def D(): # revu

    left(90)
    forward(100)
    right(90)

    for i in range(158):

        right(1.15)
        forward(1)

    penup()
    right(180)
    forward(70)
    pendown()

def E(): # revu

    down()
    left(90)
    forward(100)
    right(90)
    forward(40)
    left(180)
    forward(40)
    left(90)
    forward(50)
    left(90)
    forward(40)
    left(180)
    forward(40)
    left(90)
    forward(50)
    left(90)
    forward(40)
    penup()
    forward(10)
    pendown()

def F(): # revu


    left(90)
    forward(100)
    right(90)
    forward(40)
    left(180)
    forward(40)
    left(90)
    forward(50)
    left(90)
    forward(40)
    left(180)
    forward(40)
    left(90)
    forward(50)
    penup()
    left (90)
    forward(40)
    penup()
    forward(10)
    pendown()


def G() : # a revoir ++++++++++++++++++


    penup()
    forward(60)
    left(90)
    forward(70)
    pendown()
    forward(15)

    for i in range(120):

        left(1.5)
        forward(1)

    forward(60)

    for i in range(120):

        left(1.5)
        forward(1)

    forward(10)
    left(90)
    forward(20)
    left(180)
    forward(40)
    penup()
    forward(10)
    pendown()

def H():

    left(90)
    forward(100)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(100)
    penup()
    forward(10)
    pendown()
    penup()
    forward(10)
    pendown()

def I(): #revoir

    forward(50)
    penup()
    left(180)
    forward(25)
    right(90)
    pendown()
    forward(100)
    left(90)
    forward(25)
    penup()
    left(180)
    forward(15)
    pendown()
    forward(25)
    penup()
    right(90)
    forward(100)
    left(90)
    penup()
    forward(10)
    pendown()
    penup()
    forward(10)
    pendown()


def J() :  # test verified

    penup()
    forward(40)
    left(90)
    forward(30)
    pendown()
    forward(70)
    left(90)
    forward(30)
    left(180)
    forward(60)
    left(180)
    forward(30)
    left(90)
    forward(70)

    for i in range(55):

        right(3)
        forward(1)

    penup()
    right(105)

    forward(80)
    right(90)
    forward(15)
    left(90)

    pendown()

def K() :

    left(90)
    forward(100)
    left(180)
    forward(50)
    left(145)
    forward(65)
    left(180)
    forward(65)
    left(80)
    forward(65)
    penup()
    forward(10)
    pendown()

def L() :

    left(90)
    forward(100)
    left(180)
    forward(100)
    left(90)
    forward(50)
    penup()
    right(90)
    forward(10)
    left(90)
    forward(10)
    pendown()

def M() :

    left(90)
    forward(100)
    right(135)
    forward(50)
    left(90)
    forward(50)
    right(135)
    forward(100)
    left(90)
    penup()
    forward(10)
    pendown()
    done()

def N():

    pendown()
    left(90)
    forward(100)
    right(145)
    forward(120)
    left(145)
    forward(90)
    penup()
    left(180)
    forward(100)
    left(90)
    forward(10)
    pendown()
    penup()
    forward(10)
    pendown()

def O() : #revoir

    left(90)
    penup()
    forward(30)
    pendown()
    forward(40)

    for i in range (90):

        right(2)
        forward(1)

    forward(40)

    for i in range(90) :

        right(2)
        forward(1)

    penup()
    forward(10)
    pendown()

def P() :

    left(90)
    forward(100)
    right(90)

    for i in range(90):

        right(2)
        forward(1)

    penup()
    forward(10)
    pendown()

def Q() :

    left(90)
    penup()
    forward(30)
    pendown()
    forward(40)

    for i in range (90):

        right(2)
        forward(1)

    forward(40)
    for i in range(90) :

        right(2)
        forward(1)

    right(90)
    penup()
    forward(30)
    right(45)
    pendown()
    forward(50)
    penup()
    forward(10)
    pendown()

def R():

    left(90)
    forward(100)
    right(90)

    for i in range(90):

        right(2)
        forward(1)

    left(90)
    left(45)
    forward(60)
    penup()
    forward(10)
    pendown()

def S() :

    forward(20)

    for loop in range(60):

        forward(1.25)
        left(3)

    for loop in range(70):

        forward(1.25)
        right(3)

    penup()
    left(30)

    forward(50)
    right(90)
    forward(95)
    left(90)
    pendown()


def T() :

    penup()
    forward(50)
    pendown()
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(180)
    forward(100)
    penup()
    right(90)
    forward(100)
    left(90)
    pendown()
    penup()
    forward(10)
    pendown()

def U() :

    penup()
    left(90)
    forward(100)
    left(180)
    pendown()
    forward(60)

    for i in range (90):

        left(2)
        forward(1)

    forward(60)
    penup()
    right(180)

    forward(100)
    left(90)
    forward(10)
    pendown()

def V():

    left(90)
    penup()
    forward(100)
    right(155)
    pendown()
    forward(100)
    left(130)
    forward(100)
    right(155)
    penup()
    forward(100)
    left(90)
    pendown()
    penup()
    forward(10)
    pendown()

def W() :

    penup()
    left(90)
    forward(100)
    right(165)
    pendown()
    forward(100)
    left(145)
    forward(100)
    right(140)
    forward(100)
    left(145)
    forward(100)
    penup()
    forward(10)
    pendown()

def X(): #revoir

    left(45)
    forward(100)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(100)
    penup()
    forward(10)
    pendown()

def Y() :

    left(60)
    forward(50)
    a = position()
    forward(50)
    penup()
    setx(a[0])
    sety(a[1])
    pendown()
    left(70)
    forward(50)
    penup()
    forward(10)
    pendown()

def Z() :

    forward(50)
    left(130)
    forward(90)
    right(130)
    forward(50)
    penup()
    forward(10)
    pendown()

def espace():
    up()
    forward(70)
    down()

def apostrophe():
    up()
    forward(10)
    left(90)
    forward(80)
    down()
    right(55)
    forward(40)
    up()
    right(180-55)
    forward(100)
    left(90)
    forward(10)
    down()




def f(c,t):

    if 0 <= t <= 1:

        return c[0]*(1-t) + t*c[1]

    else:

        return vector(c[1])

def gradient(c1, c2, delta=0.1):

    s = 0
    grad = []
    while s <= 1:

        r,g,b = f([c1,c2],s).ic().toList()

        color(r,g,b)
        forward(727)
        up()
        right(90)
        forward(demi_tour)
        right(90)
        forward(727)
        left(90)
        up()
        forward(demi_tour)
        left(90)
        down()
        down()
        s+= delta


if info_grad.lower() == "oui":

    if preset_info != 1:

        for i in range(nb_color):

            exec(f"(x{i},y{i},z{i}) = input('couleur n°{i+1}(format:r,g,b) : ').split(',')")

def pos(pl):

    penup()
    setx(0)
    sety(-50)
    setx(pl)
    right(90)
    pendown()



colormode(255)

if info_grad.lower() == "oui":

    penup()
    setx(-650)
    sety(-400)
    pendown()
    left(90)
    pendown()
    speed(0)
    pensize(taille)
    down()

elif info_grad.lower() == "non":

    pos(pl)
    left(180)
    pensize(6.5)

if info_grad.lower() == "oui":

    for i in range(nb_color-1):

        exec(f"gradient(vector(float(x{i}),float(y{i}),float(z{i})), vector(float(x{i+1}),float(y{i+1}),float(z{i+1})), delta )")

if texte_info.lower() == "oui":
    pos(pl)

"""couleur du texte """
couleur_texte = couleur_texte.lower()
if couleur_texte == "other":

    colormode(255)
    r,v,b = int(input("entre ta couleur en mode 255,255,255 : \n")).split(",")
    color(r,v,b)

elif couleur_texte == "rouge":

    color(255,0,0)

elif couleur_texte == "vert":

    color(0,255,0)

elif couleur_texte == "bleu" :

    color(0,0,255)

elif couleur_texte == "noir":

    color(0,0,0)


"""/couleur du texte"""


"""affichage du texte"""
for i in range(len(texte)):
    if texte[i] == "\'":
        textef.append(apostrophe())
    else:
        textef.append(texte[i] + "()")

print(textef)
pendown()

for i in range(len(texte)):
    speed(0)

    if texte[i] == " ":
        espace()

    eval(textef[i])
    pendown()
"""/affichege du texte"""











"""
############# test

#TODO


#pip alphabet.py

#max lettre = 60px   -600 600  =20 lettre
from turtle import *


nbl = int(input("combien de lettre veux-tu ecrire : \n"))
pl = (nbl*-60)/2

def pos(pl):
    penup()
    setx(pl)
    pendown()
pos(pl)

done()

texte = input("entre le texte a écrire : \n")

for i in texte:
    exec(f"i()")

for i in (texte):
    if i == "A":
        exe = 1
    elif i == "B":
        exe = 2
    elif i == "C":
        exe = 3
    elif i == "D":
        exe = 4
    elif i == "E":
        exe = 5
    elif i == "F":
        exe = 6
    elif i == "G":
        exe = 7
    elif i == "H":
        exe = 8
    elif i == "I":
        exe = 9
    elif i == "J":
        exe = 10
    elif i == "K":
        exe = 11
    elif i == "L":
        exe = 12
    elif i == "M":
        exe = 13
    elif i == "N":
        exe = 14
    elif i == "O":
        exe = 15
    elif i == "P":
        exe = 16
    elif i == "Q":
        exe = 17
    elif i == "R":
        exe = 18
    elif i == "S":
        exe = 19
    elif i == "T":
        exe = 20
    elif i == "U":
        exe = 21
    elif i == "V":
        exe = 22
    elif i == "W":
        exe = 23
    elif i == "X":
        exe = 24
    elif i == "Y":
        exe = 25
    elif i == "Z":
        exe = 26
"""