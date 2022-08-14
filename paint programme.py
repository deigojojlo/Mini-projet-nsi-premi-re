'''
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfile
from PIL import ImageGrab

root = Tk()
root.geometry("1000x1000")
root.minsize(300,300)
root.title("paint")
cframe = Frame(root)
can = Canvas(root, width= 900, height = 900, bg = 'light grey')

old_x = None
old_y = None
arret = 0
size = 10
color = "black"
erase = "ligth grey"

def drawM(event):
    global size,color, old_x,old_y
    size = scale.get()
    if old_x and old_y :
        can.create_line(old_x,old_y,event.x,event.y,fill = color,width = size,capstyle=ROUND, smooth=TRUE, splinesteps=36)
    old_x = event.x 
    old_y = event.y

def draw(event):
    global old_x,old_y,size
    if old_x and old_y :
        can.create_oval(old_x - size,old_y-size,old_x+size,old_y+size,fill = color, width = size ,capstyle=ROUND, smooth=TRUE, splinesteps=36 )

def couleur():
    global color 
    color = askcolor()
    color = color[1]
    print(color)

def reset(event):
    global old_x, old_y
    old_x = None
    old_y = None

def effacer():
    global color,erase
    color = erase

def penstyle():
    global color
    color = 'black'

def save_button():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt'),
            ('Image', '*.png')]
    
	file = asksaveasfile( "can",filetypes = files, defaultextension = files)


def bucket():
    global color, erase
    erase = color
    can.config(bg= color)

def square():
    global color

def circle():
    global color


bcolor = Button(cframe, text = "color", command= couleur)
bcolor.grid(row = 0, column = 4)
scale = Scale(root,from_=1, to = 20, orient=VERTICAL)
pen = Button(cframe,text="pen",command= penstyle)
pen.grid(row=0, column = 2)
erase = Button(cframe, text="erase", command= effacer)
erase.grid(row=0, column= 3)
scale.pack(anchor = NE, side= RIGHT)
save_it = Button(cframe,text= "save", command= save_button)
save_it.grid(row = 0, column= 1)
tool_bucket = Button(cframe,text = "bucket", command= bucket)
tool_bucket.grid(row = 0 , column = 0)
can.bind("<Button1-Motion>",drawM)
can.bind("<Button-1>", draw)
can.bind("<ButtonRelease-1>", reset)

cframe.pack()
can.pack()
root.mainloop()
'''

from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,width=self.line_width, fill=paint_color,capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
