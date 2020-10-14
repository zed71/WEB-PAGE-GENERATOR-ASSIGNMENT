

from tkinter import *
import tkinter as tk


import python_html
import website_gui
import website_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)

        website_func.center_window(self,600,400)
        self.master.title("Set Body Text")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: website_func.os._exit(0)(self))
        arg = self.master

        website_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
