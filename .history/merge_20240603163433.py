import speech_recognition as sr
import pyttsx3,time
import webbrowser
from hacked import *
# from weather import *
from music import music_main
from data import cities,webs
from whatsapp import open_whatsapp

recognizer = sr.Recognizer()

def take():
    mic = sr.Microphone(sample_rate=48000, chunk_size=2048)
    with mic as source:
        listening_duration=3
        audio = None
        start_time = time.time()
        # while (time.time() - start_time) < listening_duration:
        try:
            # Adjust for ambient noise (optional)
            recognizer.adjust_for_ambient_noise(source,duration=3)  # Adjust duration as needed

            print("Speak now...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None
        #  Recognize speech using Google Speech Recognition
        if audio is None:
            print("please say something ")
        try:
            text = recognizer.recognize_google(audio,)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            return retry_recognition(recognizer, source)  # Offer retry option
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None
            # print(text2)
            # return text2.lower()
def tts(text):
    eng=pyttsx3.init()
    eng.say(text)
    eng.runAndWait()


def retry_recognition(recognizer, source):
    
    print("Recognition failed. Do you want to retry? (y/n)")
    response = input("> ").lower()
    if response == 'y':
        return take()
    else:
        print("Speech recognition cancelled.")
        return None

# Example usage
# # text = take()
# if text:
#     print("Lowercased text:", text)
while True:
    text=take()
    # excepquiry: ")
    text_list=text.split()
    print(text_list)
    try:
        if "open" in text:
            for web in webs:
                if web.lower() in text:
                    webbrowser.open(f"https://www.{web.lower()}.com")
                    tts(f"open {web}")
        elif "search" in text:
            index_of_search=text.find("search")
            text_list.remove("search")
            search="+".join(text_list)
            
            print(search)
            webbrowser.open(F"https://www.google.com/search?q={search}")
               


            # tts(f"open to {text} searched {my_list[1]}")
        elif "play" in text.lower():
            music_main()
            #play music
        elif "stop" or "exit" in text:
            #out of loop
            break
        elif "hack" in text_list.lower():
            #using pyauto gui
            hack_in_process()
        # elif "weather" in text:
        #     for city in cities:
        #         if city.lower() in text:
        #             print(city)
        #             tts(f'in {city} temprature is {get_current_weather(city.lower())}')
        #             #temprature of city 
        elif "hello" in text.lower():
            if "to" and "hello" and "send" not in text:
                raise ValueError("1:format is rong:massage is (your massage) send to (person name)")
            user_msg=text.split(" ")
            if "to" in text:
                index_str=user_msg.index("to")
                if index_str!= -1:
                    person=user_msg[index_str+1]
                    person=person +" "
                    print("person is ",person)
                else:
                    print("enter any person name ")
                
            if "hello" in text:
                msg=""
                index_str2=user_msg.index("hello")
                if index_str2 != -1:
                    for i, var_msg in enumerate(user_msg):
                        if i==index_str2+1:
                            msg=msg+" "+var_msg
                            index_str2+=1
                   
                    index_str3=msg.find("send")
                    if index_str3!=-1:
                        msg2=msg[:index_str3+len("send")-4]
                    
                    print("message is ",msg2)
            tts(f"message is {msg2} to send {person}")
            open_whatsapp(person,msg2)

            # process1=multiprocessing.Process(target=open_whatsapp,args=(person,msg2))
            # process2=multiprocessing.Process(target=tts,args=(f"massage is {msg2} to send {person}"))
            # process1.start()
            # process2.start()
            # process1.join()
            # process2.join()
                            
                    
                    # msg=user_msg[index_str2+1]
                    # open_whatsapp(person,msg)
                



    except ValueError:
        print("try again")