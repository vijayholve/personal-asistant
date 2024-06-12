from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from.models import persons
# Create your views here.
def home(request):
    
    if request.method == 'POST' and 'excel_file' in request.FILES:
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
    return render(request, 'home.html')