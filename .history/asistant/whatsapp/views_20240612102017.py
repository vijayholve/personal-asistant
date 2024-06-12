from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from.models import persons
# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES[fr'C:\Users\Vijay\Downloads\contacts.csv']:
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)

        # Extract specific columns
        specific_columns = df[['Name', 'Phone 1 - Value']]

        # Iterate over DataFrame rows and save data to the database
        for index, row in specific_columns.iterrows():
            persons.objects.create(
                user=request.user,
                name=row['Name'],
                phone_no=row['Phone 1 - Value']
            )
        return redirect("home")
    return render(request, 'home.html')