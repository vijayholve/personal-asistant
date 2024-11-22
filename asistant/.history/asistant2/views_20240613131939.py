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

recognizer = sr.Recognizer()

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
    text_list = text.split()
    try:
        for web in webs:
            if web.lower() in text:
                webbrowser.open(f"https://www.{web.lower()}.com")
                tts(f"Opening {web}")
                return f"Opening {web}"
        return "Success"
    except ValueError:
        return "Try again"
