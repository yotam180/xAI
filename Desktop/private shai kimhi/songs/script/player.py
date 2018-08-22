from mutagen.mp3 import MP3
from pygame import mixer
from random import shuffle
from threading import Thread
import recognition
import sys
import os
import time

def listen():
    time.sleep(2)
    while(True):
        text = recognition.recognize().lower()
        #text = input().lower()
        print(text)
        if(text is not ""):
            parse_command(text)
    

def parse_command(text):
    global playtime
    global flength
    global playing
    if("unpause" in text):
        playing = True
        mixer.music.unpause()
    elif("pause" in text):
        playing = False
        mixer.music.pause()
    elif("restart" in text):
        mixer.music.rewind()
        playtime = 0
    elif("next" in text):
        mixer.music.set_pos(flength)
        playtime = flength
    elif("move" in text):
        number = int(float(text.split(" ")[-1]))
        number = (number / 100) * flength
        mixer.music.set_pos(number)
    elif("volume" in text):
        number = int(float(text.split(" ")[-1]))
        mixer.music.set_volume(number)
    elif("quit" in text):
        os._exit(0)
playing = True
thread = Thread(target=listen)
thread.start()
mixer.init()
files = sys.argv[1:]
if(len(files) == 0):
    files = [i for i in os.listdir(os.getcwd()) if len(i.split(".")) > 1 and i.split(".")[1].lower() == "mp3"]
if(len(files) > 0):
    #case files are given as command line arguments -> play them    
    shuffle(files)
    for i in range(len(files)):
        playtime=0
        file = files[i]
        #Gets audio file duration
        flength = MP3(file).info.length
        
        mixer.music.load(file)
        mixer.music.play()
        while(flength > playtime):
            if(playing):
                playtime += 0.1
            '''
            os.system("cls")
            print(file.split(".")[0])
            print('time: ' + str(int(playtime)) + "|" + str(int(flength)))
            print('volume: ' + str(mixer.music.get_volume()))
            '''
            time.sleep(0.1)
    print("songs over")
