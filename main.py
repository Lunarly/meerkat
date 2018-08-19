from tkinter import Tk, Button, Frame, Entry, END

class ABC(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

root = Tk()
app = ABC(master=root)
app.master.title("Meerkat")
app.mainloop()
root.destroy()
