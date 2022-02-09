import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
listofsongs=[]
realnames=[]
global index
index=0#for choosing the first song
def directorychooser():
    directory = askdirectory() #helping to open a directory /file
    os.chdir(directory)#helps to enter that directory/file
    for file in os.listdir(directory):
        # only add them if they end with .mp3
        if file.endswith(".mp3"):
            realdir=os.path.realpath(file)
            #load the meta data of the file into audio variable(a dictionary)
            audio=ID3(realdir)
            #TIT2 Reffers to the title of the song
            realnames.append(audio['TIT2'].text[0])#or realnames.append(audio.get('TIT2')) if key error tit2 comnes
            listofsongs.append(file)
    #initilize pygame
    pygame.init()
    #load first song
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

def stopsong():
    pygame.mixer.music.stop()

def nextsong():
    global index
    global v
    try:
        index += 1
        #get the next song from the listofsongs
        pygame.mixer.music.load(listofsongs[index])
        #play it away
        pygame.mixer.music.play()
    except IndexError:
        index=0
        pygame.mixer.music.load(listofsongs[0])
       
        pygame.mixer.music.play()

def prevsong():
    global index
    global v
    try:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index = len(realnames)-1
        
              

root=Tk()
root.title("AP MUSIC PLAYER")
root.geometry("800x600+10+10")
root.config(bg='black')


label= Label(root,text='Music player',width=20,font=('arial',28,'bold'),background='cadet blue',fg='gold')
label.place(x=10,y=10)

listbox= Listbox(root,width=65,font=('arial',10,'bold'),background='black',fg='gold')
listbox.place(x=10,y=60)

nextbutton= Button(root,text='Next song',width=16,font=('Monotype Corsiva',16,'bold'),fg='blue',command=nextsong)
nextbutton.place(x=20,y=290)

previousbutton= Button(root,text='previous song',width=16,font=('Monotype Corsiva',16,'bold'),fg='blue',command=prevsong)
previousbutton.place(x=240,y=290)

stopbutton= Button(root,text='stop Music',width=16,font=('Monotype Corsiva',16,'bold'),fg='blue',command=stopsong)
stopbutton.place(x=40,y=350)
directorychooser()
realnames.reverse()
print(realnames)
for items in realnames:
    listbox.insert(0,items)
print(listofsongs)
root.mainloop()
#add forward, rewind,pause