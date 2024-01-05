#hawkeye/views.py
from django.shortcuts import render

app_name = 'hawkeye'

def home(request):
    return render(request, 'index.html')
def home2(request):
    return render(request, 'index2.html')


