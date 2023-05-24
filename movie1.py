from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.attributes('-fullscreen',True)

def play_giff():
    root.lift()
    root.attributes('-fullscreen',True)
    global img
    img = Image.open("ezgif.com-gif-maker.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("wallpaper Jarvis (mp3cut.net).mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1920,1200))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.004)
    root.destroy()
# root.destroy()
play_giff()
root.mainloop()




