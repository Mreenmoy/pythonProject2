import tkinter as tk
from tkinter import filedialog
from tkinter import *




def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def UploadAction1(event=None):
    filename1 = filedialog.askopenfilename()
    print('Selected:', filename1)


root = tk.Tk()
root.geometry("450x300")
var = StringVar()
var2= StringVar()


First_file = Label(root,text = "Select the file to be encripted",font=("Times New Roman", 11)).place(x = 40, y = 60)
Second_file = Label(root,text = "Select the Picture to be encripted",font=("Times New Roman", 11)).place(x = 40, y = 150)



button = tk.Button(root, text='Select First file', command=UploadAction).place(x=280, y=60)
button2 = tk.Button(root, text='Second file', command=UploadAction1).place(x=280,y=150)


root.mainloop()