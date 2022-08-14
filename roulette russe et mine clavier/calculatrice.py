from tkinter import *
lst = [
    ["c","<=","%","/"],
    ["7","8","9","x"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["","0",",","="]
]
tab_button = [
    [],
    [],
    [],
    [],
    []
]
texte = ""
info = 0
def reset():
    global texte, info,position
    texte = ""
    info = ""
    position = []
    label_calucl.config(text="")
    label_res.config(text="")
    return texte,info,position
    
def undo():
    global texte
    texte = texte[0:len(texte)-1]
    label_calucl.config(text=texte)
    return texte


def calcul(texte,position,info):
    val1 = int(texte[0:position[0]-1])
    val2 = int(texte[position[0]:])
    if info == "+":
        res = val1 + val2
        label_res.config(text= f"{res}")
    elif info == "-":
        res = val1 - val2
        label_res.config(text= f"{res}")
    elif info == "x":
        res = val1 * val2
        label_res.config(text= f"{res}")
    elif info == "/":
        res = val1 / val2
        label_res.config(text= f"{res}")
    elif info == "%":
        res = val1 % val2
        label_res.config(text= str(res))
    return res


position = []
def affiche_calcul(arg):
    global lst
    global texte
    global info
    global position
    if arg == "=":
        res = calcul(texte,position,info)
        print(res)
    elif arg == "+" or arg == "-" or arg == "%" or arg == "/" or arg == "x" :
        info = str(arg)
        if texte[len(texte)- 1] == arg:
            pass
        else :
            
            texte += arg
            position.append(len(texte))
    elif arg =="c":
        reset()
    elif arg == "<=":
        undo()
    else: 
        texte += arg
    

    label_calucl.config(text= texte, width= len(texte))
    return texte,info, position

#######TODO objectif calculatrice 4x5
root = Tk()

root.geometry("720x720")
root.minsize(300,300)
root.config(background="#D2D2D2")
frame_btn = Frame(root)
label_calucl = Label(root,text= "", width= 10, bg= "#D2D2D2")
label_calucl.pack(pady = 20)
label_res = Label(root, text="",bg='#D2D2D2')

#boucle création de button
for ligne in range(5):
    for colonne in range(4):
        exec(f"arg{ligne}{colonne} = lst[ligne][colonne]")
        
        exec(f"tab_button[ligne].append(Button(frame_btn,text= lst[ligne][colonne], width=10 , height=3, font= ('calibri'), command = lambda : affiche_calcul(arg{ligne}{colonne}) ))")
        tab_button[ligne][colonne].grid(row = ligne, column = colonne)







frame_btn.pack()
label_res.pack() 
root.mainloop()