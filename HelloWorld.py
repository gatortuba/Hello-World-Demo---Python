#Hello World GUI

#Import libraries
from tkinter import *
from tkinter import messagebox

import ctypes  # An included library with Python install.


#Funtion to display the message box
def HWMessageBox():
     var = messagebox.showinfo('Hello World', 'Hello World')


#Build Window
HelloWorld = Tk()
HelloWorld.title ("Hello World Demo") #Setup name of the window

HelloWorld.geometry("300x300") #Set default size

app = Frame(HelloWorld)
app.grid()

btnSayHello = Button(app, text ="Say Hello", command=HWMessageBox)#Sets up the button for the dialog
btnSayHello.grid(padx=120, pady=120)

HelloWorld.mainloop()

