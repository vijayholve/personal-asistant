from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from.models import persons
# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['C:\Users\Vijay\Downloads\contacts.csv']:
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)

        # Extract specific columns
        specific_columns = df[['Name', 'Phone 1 - Value']]

        # Iterate over DataFrame rows and save data to the database
        for index, row in specific_columns.iterrows():
            persons.objects.create(
                Name=row['Name'],
                column2=row['Phone 1 - Value']
            )
        return HttpResponse('Data uploaded successfully!')
    return render(request, 'upload.html')