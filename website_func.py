import os
from tkinter import *
import tkinter as tk


import website_gui

def center_window(self, w, h): 
    screen_width  = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit()
        
if __name__ == "__main__":
    pass
