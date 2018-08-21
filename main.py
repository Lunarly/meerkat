# import
from __future__ import print_function
from tkinter import *
from tkinter.filedialog import *
import os, sys, time, glob, ctypes, rpc
import tmdbsimple as tmdb
tmdb.API_KEY = ''


# bordel de la fenêtre ---------------------------------------------------------
root = Tk()
root.iconbitmap("meerkat.ico")
root.title("Meerkat")
user32 = ctypes.windll.user32
width = str(round((user32.GetSystemMetrics(0))/2))
height = str(round((user32.GetSystemMetrics(1))/2))
screensize = width + "x" + height
root.geometry(screensize)
button = Button

l2 = LabelFrame(root, text="Bibliothèques", padx=0, pady=0, relief="flat")
# l3 = LabelFrame(root, text="Historique", padx=10, pady=10, relief="ridge")
l4 = LabelFrame(root, text="Informations", padx=10, pady=10, relief="ridge")

var_fichier=StringVar()

""" def setpackforget():
    settings = Tk()
    setendroit = LabelFrame(settings, text="Importation", padx=10, pady=10)
    settest = LabelFrame(settings, text="Test", padx=10, pady=10) """

# inutile ----------------------------------------------------------------------
def nope():
   filewin = Toplevel(root)
   bNope = Button(filewin, text="nope")
   bNope.pack()

# options ----------------------------------------------------------------------
def options():
    settings = Tk()
    settings.iconbitmap("meerkat.ico")
    settings.title("Meerkat - Options")
    settings.geometry(screensize)

    setendroit = LabelFrame(settings, text="Importation", padx=10, pady=10)
    settest = LabelFrame(settings, text="Test", padx=10, pady=10)
    settingsmenu = LabelFrame(settings, borderwidth=0, highlightthickness=0, bg="white", width=100, text="", padx=5, pady=5)

    setendroit=button(settingsmenu, text="Importation", command=nope, relief=GROOVE).pack(fill="both")
    setpartage=button(settingsmenu, text="Partage", command=nope, relief=GROOVE).pack(fill="both")

    settingsmenu.pack(side=LEFT, fill="both", expand="no")
    setendroit.pack(side=RIGHT, fill="both", expand="yes")
    setpartage.pack(side=RIGHT, fill="both", expand="yes")


# FILETYPES = [ ("video files", "*.avi;*.wmv;*.mov;*.mkv;*.mks;*.mka;*.flv;*.rmvb", ) ]



# Frame Bibliothèque L2 --------------------------------------------------------
def lliste():

    l2.pack(side=LEFT, fill="both", expand="yes")

# Frame Historique L3
#def history():

#    l3.pack(side=RIGHT, fill="both", expand="yes")

# Frame Info L4
def info():
    l4.pack(side=RIGHT, fill="both", expand="yes")



# Frame Menu L1 ----------------------------------------------------------------

l1 = LabelFrame(root, borderwidth=0, highlightthickness=0, bg="white", width=100, text="", padx=5, pady=5)
l1.pack(side=LEFT, fill="both", expand="no")
laliste=button(l1, text="Liste", command=lliste, relief=GROOVE).pack(fill="both")
info=button(l1, text="info", command=info, relief=GROOVE).pack(fill="both")
options=button(l1, text="Options", command=options, relief=GROOVE).pack(fill="both")

# about ------------------------------------------------------------------------
def about():
    about = Tk()
    about.title('À propos')
    about.geometry("580x385")
    about.resizable(False, False)
    about.iconbitmap("meerkat.ico")
    aboutextfrm = LabelFrame(about, bg="white", width=100, text="", padx=5, pady=5)
    aboutextfrm.pack(side=RIGHT, fill="both", expand="yes")
    aboutext = Label(aboutextfrm, bg="white", text="Meerkat 1.0", font='Helvetica 15 bold', anchor=W, justify=LEFT).pack()
    aboutext = Label(aboutextfrm, bg="white", text="").pack()
    aboutext = Label(aboutextfrm, bg="white", text="Auteur:", font='Helvetica 10 bold', anchor=W, justify=LEFT).pack()
    aboutext = Label(aboutextfrm, bg="white", text="kodle, Giltham", font='Helvetica 10', anchor=W, justify=LEFT).pack()
    aboutext = Label(aboutextfrm, bg="white", text="").pack()
    aboutext = Label(aboutextfrm, bg="white", text="Contributeur:", font='Helvetica 10 bold', anchor=W, justify=LEFT).pack()
    aboutext = Label(aboutextfrm, bg="white", text="Adiboux", font='Helvetica 10', anchor=W, justify=LEFT).pack()

# selection du dossier
def selection():
    global folder
    folder = askdirectory() #title="Choisir un dossier")


# scan
global listbox
listbox = Listbox(l2, height=1000)
listbox.pack()

def scan():
    try:
        folder
    except NameError:
        selection()
    files = os.listdir(folder)
    for i in range(len(files)):
        listbox.insert(END, files[i])
    global active_listbox
    active_listbox = listbox.get('active')
    #AFFICHER LA PAGE DE LACTIVE
    root.update()
    page(active_listbox)

def page(active_listbox):
    while True:
        if listbox.get('active') == active_listbox:
        #AFFICHER NOUVELLE PAGE AVEC INDEX
            root.update()
        else:
            active_listbox = listbox.get('active')
            print(active_listbox)


def path():
    files_path = folder + "\\" + active_listbox
    print(files_path)
    return files_path

def openf():
    p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe"]) #,"file://])



# menu -------------------------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
helpmenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Scan", command = scan)
filemenu.add_command(label = "Selectioner un dossier", command = selection)
filemenu.add_separator()
filemenu.add_command(label = "Quitter", command = root.quit)
menubar.add_cascade(label = "Fichier", compound=LEFT, menu = filemenu)

helpmenu.add_command(label = "À propos", command = about)
helpmenu.add_command(label = "Support", command = nope)
helpmenu.add_separator()
helpmenu.add_command(label = "Mise à jour", command = nope)
menubar.add_cascade(label = "Help", compound=LEFT, menu = helpmenu)

editmenu = Menu(menubar, tearoff=0)
root.config(menu = menubar)


root.mainloop()
