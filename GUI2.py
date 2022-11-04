import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("500x500")
listsample = Listbox(root,width=70,height=30,
fg="red",font=("Arail 28"))
listsample.insert(1,"pizza")
listsample.insert(2,"pizza 1")
listsample.insert(3,"pizza 2")

listsample.pack()
root.mainloop()