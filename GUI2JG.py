# This imports the tkinter "tool box" this contains
#all the support material to make GUI elements. 
#by including "as tk" we are giving a short name to use
import tkinter as tk 


root = tk.Tk()


#*******WIDGET 1*******
#THree stages to build elements/objects
#!. CONSTRUCT the Object: we build and configure it.
#2. Configure the Object: we specify behaviours ad settings (OPTIONAL)
#3 PAck the Object: PUt it in the window
titleLabel = tk.Label(root, text = "PASSWORD GENERATOR", font = ("Avenir", 16))
#Ordered parameters: THe order we send them matters. (COMMON)
#named parameters: JavaScript and Python specific
titleLabel.grid(row = 0, column = 0, columnspan = 2)

#*******WIDGET 2 (TEXT)*******
output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)

#*******WIDGET 3 (LABELS)*******
word1Label = tk.Label(root, text = "Word 1", background = "red", foreground = "blue")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

word2Label = tk.Label(root, text = "Word 2", background = "red", foreground = "blue")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = "Word 3")
word3Label.grid(row = 4, column = 0)

#*******WIDGET 4 (ENTRY)*******
ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

#*******WIDGET 5 (BUTTONS)*******
btnGo = tk.Button(root, text = "GENERATE")
btnGo.grid(row = 5, column = 1)




#We are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program