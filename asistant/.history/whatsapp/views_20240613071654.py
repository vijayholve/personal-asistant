from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd # type: ignore
from.models import persons
# Create your views here.
def home(request):
    q=request.GET.get("q") if request.GET.get("q") else ''
    person=persons.objects.all()
    if q:
        person=persons.objects.filter(name__icontains=q)
    if request.method == 'POST' and 'excel_file' in request.FILES:
        return _extracted_from_home_4(request)
    content={"persons":person}
    return render(request, 'whome.html',content)


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
    process_speech(request)
    return render(request, 'index.html')

recognizer = sr.Recognizer()


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr

@csrf_exempt
def process_speech2(request):
    if request.method == 'POST':
        data = request.POST.get('text', '')

        # Process the received speech data (text) as needed
        if data:
            # Example: Save the speech data to a model or perform some action
            # For demonstration, we'll echo back the received text
            response_data = {
                'status': 'success',
                'message': f'You said: {data}',
            }
        else:
            response_data = {
                'status': 'error',
                'message': 'Speech data not received.',
            }
        
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

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
    text_list = text.split()
    print(text_list)

    try:
        if "open" in text:
            for web in webs:
                if web.lower() in text:
                    webbrowser.open(f"https://www.{web.lower()}.com")
                    tts(f"Opening {web}")
        elif "search" in text:
            _extracted_from_process_text_12(text)
        elif "play" in text:
            music_main()
        elif "stop" in text or "exit" in text:
            return
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
                print("Format is wrong: message is (your message) send to (person name)")
                tts("Format is wrong: message is (your message) send to (person name)")
    except ValueError:
        print("Try again")
        tts("Try again")


# TODO Rename this here and in `process_text`
def _extracted_from_process_text_12(text):
    index_of_search = text.find("search")
    search_terms = text[index_of_search + len("search"):].strip()
    search_query = "+".join(search_terms.split())
    print(search_query)
    webbrowser.open(f"https://www.google.com/search?q={search_query}")
    tts(f"Searching for {search_terms}")

def tts(text):
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()