import cv2
import datetime
import tkinter as tk
from tkinter import *
from pytube import YouTube
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog

def CreateWidgets():
    linkLabel = Label(root,text="Youtybe Link  :",bg = "tan4" )
    linkLabel.grid(row=1,column=0,padx=5,pady=5)

    root.linkText = Entry(root,width=57,textvariable=videoLink)
    root.linkText.grid(row=2,column=1,pady=5,padx=5,columnspan=2)

    destinationLabel = Label(root,Text= "Destination   :",bg="tan4")
    destinationLabel.grid(row=2,column=0,padx=5,pady=5)

    root.destinationText = Entry(root,width=40,textvariable=downloadPath)
    root.destinationText.grid(row=2,column=1,pady=5,padx=5)

    browseButton = Button(root , text = "BROWSE" , command=Browse,width=15)
    browseButton.grid(row=2,column=2,padx=5,pady=5)

    dwldButton = Button(root,text="DOWNLOAD",command=Downlaod,width=30)
    dwldButton.grid(row=3,column=1,padx=5,pady=5)

    root.videoLabel = Label(root,bg='tan4')
    root.videoLabel.grid(row=4,column=0,columnspan=3,pady=5,padx=5)



root = tk.Tk()
root.geometry("665x490")
root.title("Sasi\'s Creations")
root.config(background="tan4")
root.resizable(False,False)
