from django.urls import path
from . import views

app_name = 'patrol'

urlpatterns = [
    path('', views.home, name='home')
]
