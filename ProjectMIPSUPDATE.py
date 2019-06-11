import os
import shutil
import glob
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk


class FileGen: #Create Class 


	def __init__(self, path): #initialize itself and the parameter "path", constructor in object-oriented programming


#Create the folders

		folder("*.py","Python Scripts")
		folder("*.html","HTML")
		folder("*.mp3","Music")
		folder("*.mp4","Videos")
		folder("*.txt","Documents/Text Files")
		folder("*.docx","Documents/Word Files")
		folder("*.pptx","Documents/PowerPoint Presentations")
		folder("*.pdf","Documents/PDF Files")
		images=["*.jp*","*.png","*.psd","*.bmp"]

		for img in images: #This addition just allows the program to be able to encompass more filetypes
			folder(img,"Images") 



	# Copying Files
	def copy(self,newpath,file): #Define the method "copy"
		if not os.path.exists(newpath): #Checks if the folder exists
		    os.makedirs(newpath) #Recursive directory creation function
		shutil.copy(file, newpath) #Copies the existing file to the the new directory
		os.remove(file) #Removes the original file

#The program doesn't actually "move" the file, instead it duplicates it and deletes the old file

# Creating Folders
	def folder(self, extension,foldername): #Define the method "folder" and create parameters extension and foldername
		lists=glob.glob(extension) #Recursively lists out the file names
		for name in lists: #Range loop which takes all the file names and then makes a folder based on what extensions
			copy(foldername,name) #there are in the directory

#Sorting Files




root = tk.Tk() #Create an instance of Tk which creates the base window
root.geometry('300x600') #Define the file window size, so it won't be defined by the widgets

def FileSorter(): #Define the back end as a method
	print("File Sorter")
	#pull path 
	f = FileSorter(path) #Create an object (variable) and tie it to the method and the parameter path


def darkcolors():
	root.config(bg='gray13')
	label1.config(bg='gray13')
	label1.config(fg='dodgerblue2')
	lbl1.config(fg='deep sky blue')
	lbl1.config(bg='gray13')
	button2.config(fg='black', bg = "black")
	darkbutton.config(bg='gray13')
	lightbutton.config(bg='gray13')
	line1.config(bg='gray13')
	line1.config(fg='white')
	line2.config(bg='gray13')
	line2.config(fg='white')
	line3.config(bg='gray13')
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


executebutton=Button(root, text="Sort!", bg = "dodgerblue", font = ("Avenir Black", 24), padx = 35, pady = 15, command = FileSorter)
executebutton.grid(column = 0, row = 8, padx = 10, pady = 10)
root.mainloop()


