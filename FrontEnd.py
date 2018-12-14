
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.geometry('300x600')

def FileSorter():
	import BackEnd.py

def darkcolors():
	root.config(bg='gray13')
	label1.config(bg='gray13')
	label1.config(fg='dodgerblue2')
	lbl1.config(fg='deep sky blue')
	lbl1.config(bg='black')
	button2.config(fg='black', bg = "black")
	darkbutton.config(bg='gray13')
	lightbutton.config(bg='gray13')
	line1.config(bg='black')
	line1.config(fg='white')
	line2.config(bg='black')
	line2.config(fg='white')
	line3.config(bg='black')
	line3.config(fg='white')


def lightcolors():
	root.config(bg='white')
	label1.config(bg='white')
	label1.config(fg='navy')
	lbl1.config(bg='white')
	lbl1.config(fg='black')
	line1.config(bg='white')
	line1.config(fg='dodgerblue')
	line2.config(bg='white')
	line2.config(fg='dodgerblue')
	line3.config(bg='white')
	line3.config(fg='dodgerblue')
	button2.config(fg='black', bg='white')

#Directory choosing
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

#Title
root.title("FileSorter")

#Label Title
label1 = tk.Label(root, text="FileSorter", fg="navy", font=("Avenir Black", 50), padx = 30, pady = 20)
label1.grid(column = 0, row = 0)

#Accessibility

darkbutton=Button(root,text="Dark mode", command=darkcolors)
darkbutton.grid(column=0,row=2, ipadx = 10, ipady = 10, padx =10, pady = 10)


lightbutton=Button(root,text="Light mode", command=lightcolors)
lightbutton.grid(column=0,row=3, ipadx = 10, ipady = 10, padx = 10, pady = 10)




#Divider

line1 = Label(root, text = "________ Accessibility _______", fg= 'dodgerblue', font = ('Avenir Heavy', 14))
line1.grid(column = 0, row = 1, padx = 10, pady = 10)
line2 = Label(root, text = "______ Choose Directory ______", fg = "dodgerblue", font = ("Avenir Heavy", 14))
line2.grid(column = 0, row = 4, padx = 10, pady = 10)
line3 = Label(root, text = "_____________ Run ____________", fg = "dodgerblue", font = ("Avenir Heavy", 14))
line3.grid(column = 0, row = 7, padx = 10, pady = 10)

folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path, font = ("Avenir Heavy", 14))
lbl1.grid(column=0, row=5, padx = 10, pady = 10)
button2 = Button(text="Browse", command=browse_button)
button2.grid(column=0, row=6, ipadx = 10, ipady = 10)


executebutton=Button(root, text="Sort!", bg = "dodgerblue", font = ("Avenir Black", 24), padx = 35, pady = 15)
executebutton.grid(column = 0, row = 8, padx = 10, pady = 10)
root.mainloop()


