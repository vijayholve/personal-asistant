import pygame
import os
import random
import speech_recognition as sr


recn = sr.Recognizer()


arr=list(range(1,12))
# music_file = "C:/Users/Rayat/Downloads/pepperfry/vijay_proj/a.mp3"
def play_music(music):
    pygame.init()
    try:
        pygame.mixer.music.load(f"C:\Users\Vijay\Pictures\MERN_VIJAY\0{music}. HTML (Level 1) - Part B.mp3")
    ex
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            query=input("change/pause :")
            if "pause" in query:
                        pygame.mixer.music.pause()
                        
            elif "change" in query:
                        pygame.mixer.music.pause()
                        rand2=random.choice(arr)
                        play_music(rand2)
            else:
                        print("nothing")

def music_main():
    rand=random.choice(arr)

    play_music(rand)

    pygame.quit()
    
music_main()
