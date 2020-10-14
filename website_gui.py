

from tkinter import *
import tkinter as tk


import website_main
import website_func


def load_gui(self):

    self.lbl_bodyt = tk.Label(self.master,text='Body Text:')
    self.lbl_bodyt.grid(row=0, column=0, padx=(27,0), pady=(10,0),sticky=N+W)
    

    self.txt_bodyt = tk.Entry(self.master, text='')
    self.txt_bodyt.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    

    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: website_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

    
    self.btn_update = tk.Button(self.master, width=12, height=2, text='Update', command={myaction}.root.bind('<Return>', lambda e: action.invoke())
    self.btn_update.grid(row=10, column=1, padx=(15,0), pady=(45,10), sticky=W)

    website_func.create_db(self)
    website_func.onRefresh(self)

    if __name__ == "__main__":
        pass
