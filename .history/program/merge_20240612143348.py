import speech_recognition as sr
import pyttsx3
import time
import webbrowser
from hacked import hack_in_process
# from weather import *
from music import music_main
from data import cities, webs
from whatsapp import open_whatsapp

recognizer = sr.Recognizer()

def take():
    mic = sr.Microphone(sample_rate=48000, chunk_size=2048)
    with mic as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=3)  # Adjust duration as needed
            print("Speak now...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"An error occurred while listening: {e}")
            return None

        try:
            text = recognizer.recognize_google(audio, language="en-IN")
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            return retry_recognition()
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"An error occurred during recognition: {e}")
            return None

def tts(text):
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()

def retry_recognition():
    print("Recognition failed. Do you want to retry? (y/n)")
    response = input("> ").lower()
    if response == 'y':
        return take()
    print("Speech recognition cancelled.")
    return None

def main():
    while True:
        text = take()
        if not text:
            continue

        text_list = text.split()
        print(text_list)

        try:
            if "open" in text:
                for web in webs:
                    if web.lower() in text:
                        webbrowser.open(f"https://www.{web.lower()}.com")
                        tts(f"Opening {web}")
            elif "search" in text:
                index_of_search = text.find("search")
                search_terms = text[index_of_search + len("search"):].strip()
                search_query = "+".join(search_terms.split())
                print(search_query)
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                tts(f"Searching for {search_terms}")
            elif "play" in text:
                music_main()
            elif "stop" in text or "exit" in text:
                break
            elif "hack" in text.lower():
                hack_in_process()
            # elif "weather" in text:
            #     for city in cities:
            #         if city.lower() in text:
            #             print(city)
            #             tts(f'in {city} temperature is {get_current_weather(city.lower())}')
            elif "hello" in text:
                if "to" in text:
                    parts = text.split(" to ")
                    msg_part = parts[0].replace("hello", "").strip()
                    person = parts[1].strip()
                    tts(f"Message is {msg_part} to send to {person}")
                    open_whatsapp(person, msg_part)
                else:
                    print("Format is wrong: message is (your message) send to (person name)")
                    tts("Format is wrong: message is (your message) send to (person name)")
        except ValueError:
            print("Try again")
            tts("Try again")

m ain() 
