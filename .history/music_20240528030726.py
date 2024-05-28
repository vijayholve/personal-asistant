import pygame
import os
import random
import speech_recognition as sr
import os ,glob
directory = 'C:/Users/Vijay/Pictures/MERN_VIJAY/09. HTML (Level - 3)'
print(directory)
# Get a list of all files in the directory
files = glob.glob(os.path.join(directory, '*'))

# Loop through and process each file

# music_file = "C:/Users/Rayat/Downloads/pepperfry/vijay_proj/a.mp3"
def play_music(music):
    pygame.mixer.init()
    
    pygame.mixer.music.load(music)
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            query=input("change/pause :")
            if "pause" in query:
                        pygame.mixer.music.pause()
                        
            elif "change" in query:
                        pygame.mixer.music.pause()
                        rand2=random.choice(files)
                        play_music(rand2)
            else:
                        print("nothing")

def music_main():
    # a=+/
    # rand=random.choice(files)
    # print(rand)
    
    # print("replaced",file)
    play_music("c:\Users/Vijay/Pictures/MERN_VIJAY/09. HTML (Level - 3)+/04. Practice Qs.mp4")
    
    # pygame.quit()
    
music_main()
