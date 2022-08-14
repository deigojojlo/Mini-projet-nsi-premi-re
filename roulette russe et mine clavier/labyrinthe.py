from tkinter import *                                               #import
from random import randint ,choice
from time import sleep

tab = []
tab_dico = []
taille = 0


root = Tk()                                                         #config de la fenetre
root.geometry("650x650")
root.minsize(200,200)
root.title("labyrinthe")
Laby = Canvas(root,width= 600, height=600, bg= "#F6FFB3")




def init(x:int) -> None:                                                        #initialise le jeu
    global tab,tab_dico,taille
    tab , tab_dico = init_laby(x, x)
    taille = init_canvas(x, x)
    Laby.pack()
    Laby.config()
    affiche_laby(tab)
#prend en argument le nombre de cases de côté





def get_entry(event) -> int:
    global x
    x = int(nb.get())
    nb.delete(0,)
    nb.destroy()
    texte.destroy()
    init(x)
    return x
#evenement qui va initialiser tout le canvas
#après avoir ressus l'information du nombre de cases de côté
#return le nombre de cases de longueur du tableau
    

def init_laby(x:int,y:int) -> list:
    tab = [[k * x + i for i in range(y)] for k in range(x)]         #creation de tab
    tab_dico = [[ 0 for i in range(x)] for k in range(y)]           #creation de tab_dico
    for i in range(len(tab)):                                       #boucle pour integrer les dicos au tab_dico
        for k in range(len(tab[0])):
            tab_dico[i][k] = {"id" : tab[i][k], "D":True, "B" : True}
    return tab , tab_dico
#prend en argument les abscisses et les ordonnés 
#creer le tableau tab qui contient les id de chaque case
#creer le tableau de dictionnaire tab_dico qui contient les informations des cases 
#return nos tableaux 



def init_canvas(x:int,y:int) -> int:                                       #dessine notre grille en fonction de notre entrer initial
    l = int(600/x)                         
    taille = l                                                      #taille definie la longueur et la largeure d'une case
    for i in range(0,620,l):    
        Laby.create_line(0,i,600,i)
        Laby.create_line(i,0,i,600)
    return taille 
#prend en argument les abscisses et les ordonnés 
#creer le tableau dans le canvas Laby
#return la taille en abscisse et en ordonné des cases



def affiche_laby(tab:list) -> None:                                        
    for i in range(len(tab)):
        print(tab[i])
#affiche plus clairement notre tableau avec les ids
#utilise tab pour l'afficher ligne par ligne
#return None



def voisin(case:tuple,position:str,taille:int) -> tuple:                                 #retransmet le dico de la case voisin et les coo du mur entre les deux cases
    l = case[0]
    h = case[1]
    if position == 'D':
        return tab_dico[l][h+1],(l+1)*taille,h*taille,(l+1)*taille,(h+1)*taille
    elif position == "B" :
        return tab_dico[l+1][h],l*taille,(h+1)*taille,(l+1)*taille,(h+1)*taille
    


    
def casse_mur(l:int,h:int,position:str,taille:int) -> list:
    global tab, tab_dico                                            #appel des tab
    dico_voisin,pos1,pos2,pos3,pos4 = voisin((l,h), position,taille)#appel voisin et les coo du mur
    print(dico_voisin)
    print((tab_dico[l][h]))
    if dico_voisin["id"] != (tab_dico[l][h])["id"]:                 #regarde leurs id
        (tab_dico[l][h])[position] = False                          #on change la valeur du dico
        id_voisin = dico_voisin["id"]                               #on recupère l'id du voisin
        n_id = (tab_dico[l][h])["id"]                               #on recupère l'id de la case
        Laby.create_line(pos1,pos2,pos3,pos4,fill = "#F6FFB3")      #on effaace le mur
        for x in range(len(tab)):                                   #boucle qui parcour tout le tableau
            for y in range(len(tab[0])):
                if (tab_dico[x][y])["id"] == id_voisin:             #si l'id de la case et le meme que celui de la case voisine initial
                    (tab_dico[x][y])["id"] = n_id                   #alors son id change pour celui de la case initial
                    tab[x][y] = n_id                                #et dans tab aussi
    return tab,tab_dico




def genere_laby(event) -> None:
    global x,taille,tab,tab_dico
    a = int(x**2 - x*1.90)                                       #appel de la dimension du tableau
    while a != 0:                                          #boucle 
        Laby.update()
        sleep(0.1)
        l = randint(0, x-2)                                         # genère une case 
        h = randint(0, x-2)
        if a % 2 == 0:                           #position
            position = 'D'
        else :
            position = 'B'
        if (tab_dico[l][h])['D'] == True and (tab_dico[l][h])['B'] == True:
            tab,tabdico = casse_mur(l, h, position,taille)   
            a -= 1
        else :
            pass                                                    #case le mur
        affiche_laby(tab)
    for i in range(x-1):
        for k in range(x-1):
            Laby.update()	
            if tab[i][k] != tab[i][k+1]:
                tab,tabdico = casse_mur(i, k, 'D',taille)  
            elif tab[i][k] != tab[i+1][k]:
                tab,tabdico = casse_mur(i, k, 'B',taille)  
    affiche_laby(tab)


x = 0
texte = Label(root,text= "entrez le nombre de cases de côté")
nb = Entry(root, bd = 10,relief=FLAT, )
texte.pack()
nb.pack()
root.bind('<Return>',get_entry)
print(x)






Laby.bind("<Button-1>", genere_laby)
root.mainloop()
