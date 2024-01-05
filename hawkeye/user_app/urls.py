# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('logout/', views.user_logout, name='logout'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # Add other URLs as needed
]
