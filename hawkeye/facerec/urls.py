# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_images, name='upload'),
]
