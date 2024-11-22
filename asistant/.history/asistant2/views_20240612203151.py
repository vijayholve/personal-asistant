from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
import pyttsx3
import webbrowser
from assistant.hacked import hack_in_process
from assistant.music import music_main
from assistant.data import webs
from assistant.whatsapp import open_whatsapp

recognizer = sr.Recognizer()

@csrf_exempt
def process_audio(request):
    if request.method == 'POST':
        audio_data = request.FILES.get('audio_data')
        if not audio_data:
            return JsonResponse({'error': 'No audio data received'})
        
        text = process_audio_data(audio_data)
        return JsonResponse({'response': text})
    return JsonResponse({'error': 'Invalid request method'})

def process_audio_data(audio_data):
    try:
        with sr.AudioFile(audio_data) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="en-IN")
            return text.lower()
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An error occurred during recognition: {e}"

def tts(text):
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()

def main(text):
    text_list = text.split()
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
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            tts(f"Searching for {search_terms}")
        elif "play" in text:
            music_main()
        elif "stop" in text or "exit" in text:
            return "exit"
        elif "hack" in text.lower():
            hack_in_process()
        elif "hello" in text:
            if "to" in text:
                parts = text.split(" to ")
                msg_part = parts[0].replace("hello", "").strip()
                person = parts[1].strip()
                tts(f"Message is {msg_part} to send to {person}")
                open_whatsapp(person, msg_part)
            else:
                return "Format is wrong: message is (your message) send to (person name)"
        return "Success"
    except ValueError:
        return "Try again"
