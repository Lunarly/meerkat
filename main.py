# import
from __future__ import print_function
from tkinter import *
from tkinter.filedialog import askdirectory
import os, sys

# bordel de la fenêtre
root = Tk()
root.title("Meerkat")
root.geometry("500x500")

# commande inutile
def nope():
   filewin = Toplevel(root)
   button = Button(filewin, text="nope")
   button.pack()

# selection du dossier
def selection():
    global folder
    folder = askdirectory()

# scan
def scan():
    try:
        folder
    except NameError:
        selection()
    var_label = StringVar()     #Zone de communication avec objet TkInter/Label
    label=Label(root,textvariable=var_label).pack() # Association Label et StringVar
    files = os.listdir(folder)
    for name in files:
        print(name)
        var_label.set(name)
        var_label=StringVar()
        label=Label(root,textvariable=var_label).pack()

# menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Scan", command = scan)
filemenu.add_separator()
filemenu.add_command(label = "Selectioner un dossier", command = selection)
filemenu.add_command(label = "Quitter", command = root.quit)
menubar.add_cascade(label = "Options", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)



root.config(menu = menubar)

root.mainloop()
