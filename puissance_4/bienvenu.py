from tkinter import *

fenetre = Tk()


fenetre.geometry("720x500")
fenetre.minsize(720,500)



label_salut = Label(fenetre, text="bienvenue !", font = ("calibri",15))
bouton = Button(command=exit, text= "exit", font = ("calibri", 10),width=10 )


label_salut.pack()
bouton.pack(pady= 300)



def exit():
    fenetre.destroy()




fenetre.mainloop()