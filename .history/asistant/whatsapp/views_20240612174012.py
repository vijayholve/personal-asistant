from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from.models import persons
# Create your views here.
def home(request):
    person=persons.objects.all()
    if request.method == 'POST' and 'excel_file' in request.FILES:
        return _extracted_from_home_4(request)
    content={"persons":person}
    return render(request, 'home.html',content)


# TODO Rename this here and in `home`
def _extracted_from_home_4(request):
    excel_file = request.FILES['excel_file']
    file_extension = excel_file.name.split('.')[-1]

    if file_extension == 'xlsx':
        df = pd.read_excel(excel_file, engine='openpyxl')
    elif file_extension == 'xls':
        df = pd.read_excel(excel_file, engine='xlrd')
    elif file_extension == 'csv':
        df = pd.read_csv(excel_file)
    else:
        return HttpResponse('Unsupported file format')

    # Extract specific columns
    specific_columns = df[['Name', 'Phone 1 - Value']]
    # Iterate over DataFrame rows and save data to the database
    for index, row in specific_columns.iterrows():
        persons.objects.create(

            name=row['Name'],
            phone_no=row['Phone 1 - Value']
        )
    return redirect("home")
import speech_recognition as sr
import pyttsx3
import webbrowser
from django.http import JsonResponse
from django.shortcuts import render
from program.hacked import hack_in_process
from program.music import music_main
from program.data import cities, webs
from program.whatsapp import open_whatsapp

recognizer = sr.Recognizer()

def index(request):
    return render(request, 'index.html')

recognizer = sr.Recognizer()

def index(request):
    return render(request, 'index.html')

def process_speech(request):
    if request.method == 'POST':
        text = take()
        response_data = {}
        if not text:
            response_data['status'] = 'error'
            response_data['message'] = 'Could not recognize speech. Please try again.'
        else:
            response_data['status'] = 'success'
            response_data['message'] = f'You said: {text}'
            process_text(text)
        return JsonResponse(response_data)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def take():
    mic = sr.Microphone(sample_rate=48000, chunk_size=2048)
    with mic as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=3)
            print("Speak now...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        except Exception as e:
            print(f"An error occurred while listening: {e}")
            return None

        try:
            text = recognizer.recognize_google(audio, language="en-IN")
            print("You said:", text)
            return text.lower()
        except Exception as e:
            print(f"An error occurred during recognition: {e}")
            return None

def process_text(text):
    from django.http import JsonResponse

def process_speech(request):
    if request.method == 'POST':
        try:
            # Example: Fetching data from POST request
            data = request.POST  # Adjust to your actual data handling

            # Example: Perform processing (replace with actual logic)
            text = data.get('speech_data', '')  # Example key 'speech_data'

            # Example: Return JSON response
            return JsonResponse({'text': text})

        except Exception as e:
            # Log the exception or handle it appropriately
            return JsonResponse({'error': str(e)}, status=500)

    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def tts(text):
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()