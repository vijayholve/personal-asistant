from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import speech_recognition as sr
import pyttsx3
import webbrowser
from program.hacked import hack_in_process  # Custom imports
from program.music import music_main
from program.data import webs
from program.whatsapp import open_whatsapp
from whatsapp.models import persons
recognizer = sr.Recognizer()
per_name=persons.objects.values("name")
def index(request):
    return render(request, 'asistant2/index.html')

@csrf_exempt
def process_audio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        response_message = main(text)
        return JsonResponse({'status': 'success', 'message': response_message})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def tts(text):
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()

def main(text):
    print("In main:", text)
    song=["Play","play","song","Song"]
    open=["open","Open"]
    messgae=["messages","massage","message","Messages","assage","message"]
    text_list = text.split()
    try:
        if any(o in text for o in open):
            for web in webs:
                if web.lower() in text:
                    webbrowser.open(rf"https://www.{web}.com")
                    tts(f"Opening {web}")
                    return f"Opening {web}"
        elif "Search" in text or "search" in text:
            index_of_search = text.find("search")
            search_terms = text[index_of_search + len("search"):].strip()
            search_query = "+".join(search_terms.split())
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            tts(f"Searching for {search_terms}")
            return f"Searching for {search_terms}"
        elif any(word in text  for word in song ):
            music_main()
            return "Playing music"
        elif "Stop" in text or "Exit" in text:
            return "exit"
        elif "Hack" in text.lower():
            hack_in_process()
            return "Hack in process"
        elif any(msg in text for msg in messgae):
            if "to" in text:
                parts = text.split(" to ")
                msg_part = parts[0].replace("sent", "").strip()
                person = parts[1].strip()
                
                tts(f"Message is {msg_part} to send to {person}")
                for p in per_name:
                    if p in person or p is person:
                        open_whatsapp(p.id, msg_part)
                        return f"Message is {msg_part} to send to {person}"
                return f"person is not in database"
            else:
                return "Format is wrong: message is (your message) send to (person name)"
        return "Success"
    except ValueError:
        return "Try again"
