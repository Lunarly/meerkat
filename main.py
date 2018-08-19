# import
from __future__ import print_function
from tkinter import *
import os, sys

#
root = Tk()
root.title("Meerkat")
root.geometry("300x300")

path = '.'

# commande inutile
def nope():
   filewin = Toplevel(root)
   button = Button(filewin, text="nope")
   button.pack()

# scan
var_label = StringVar()     #Zone de communication avec objet TkInter/Label
label=Label(root,textvariable=var_label).pack() # Association Label et StringVar

files = os.listdir(path)
for name in files:
    print(name)
    var_label.set(name)

# menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="test", command = nope)

filemenu.add_separator()

filemenu.add_command(label = "Quitter", command = root.quit)
menubar.add_cascade(label = "Options", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = nope)


root.config(menu = menubar)
root.mainloop()
