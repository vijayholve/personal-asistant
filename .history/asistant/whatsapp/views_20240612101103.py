from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['C:\Users\Vijay\Downloads\contacts.csv']:
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)

        # Extract specific columns
        specific_columns = df[['Column1', 'Column2']]

        # Iterate over DataFrame rows and save data to the database
        for index, row in specific_columns.iterrows():
            MyModel.objects.create(
                column1=row['Column1'],
                column2=row['Column2']
            )
        return HttpResponse('Data uploaded successfully!')
    return render(request, 'upload.html')