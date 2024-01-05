from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ML import predict
import os
import pandas as pd

from .forms import ImageForm

app_name = 'facerec'



def upload_images(request):
    data = {'Name': []}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                # Process each image - save it to the desired location or perform other operations
                # Example: You might save it to a specific directory
                upload_path = os.path.join(settings.BASE_DIR, 'uploads', image.name)
                # Save the image to the specified directory
                with open(upload_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

            # output_dict = predict('uploads', model_path='trained_knn_model.clf')  # Use your ML model function here
            for image_file in os.listdir('uploads'):
                full_file_path = os.path.join("uploads", image_file)

                predictions = predict(full_file_path, model_path = os.path.join(settings.BASE_DIR, 'facerec/trained_knn_model.clf'))

                os.remove(full_file_path)

                for name, (top, right, bottom, left) in predictions:
                    if name != 'unknown':
                        data['Name'].append(name)

            data['Name'] = list(set(data['Name']))

    if 'download' in request.GET:
        file_path = 'output.xlsx'
        with open(file_path, 'rb') as file:
            response = HttpResponse(file, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="output.xlsx"'
            return response
        
    else:
        form = ImageForm()
        
        
        
    attend = pd.DataFrame(data)
    refer = pd.read_csv('reference.csv') 
    output_file = refer.copy()
    attend['Status']='Present'
    attend=attend.drop_duplicates()
    output_file = output_file.merge(attend, on='Name', how='left')
    output_file['Status'].fillna('absent', inplace=True)
    # Save the DataFrame to an Excel file
    output_file.to_excel('output.xlsx', index=False) 
    output_html = output_file.to_html(classes='table table-striped')
    print(data)

    return render(request, 'upload_images.html', context = {'form': form,'output_html': output_html, 'names': data['Name'] })