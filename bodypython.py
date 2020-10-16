import tkinter
from tkinter import *
import webbrowser
import tkinter as tk

# code to load window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.master.title("Customize Webpage") 

        self.labelTxt = Label(text = "Customize your webpage by entering text, then click to view!", font=("Arial", 12))
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))

        # code to enter the text field
        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)
        
        self.btnSubmit = Button(self.master, text="Submit", width=12, height=1, command=self.customEntry)
        self.btnSubmit.grid(row=2, column=1, padx=(0,10) , pady=(0,10))
                                
        self.master.columnconfigure(1,weight=1)

        # code to launch browser with text
    def customEntry(self):
        customText = self.txtEntry.get()
        htmlFile = open("user_customized.html", "w")
        htmlFormat = "<html>\n<body>\n<p>" + customText + "</p>\n</body>\n</html>"
        htmlFile.write(htmlFormat)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() 
