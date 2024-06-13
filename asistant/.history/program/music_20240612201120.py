import pygame
import os
import random
import os ,glob
directory = "c:/Users/Vijay/Music"
print(directory)
# Get a list of all files in the directory
files = glob.glob(os.path.join(directory, '*'))

# Loop through and process each file


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
   
    rand=random.choice(files)
    print(rand)
    
    play_music(rand)
    
    pygame.quit()
    
music_main()