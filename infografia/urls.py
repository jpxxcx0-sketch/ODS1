from django.urls import path
from . import views

app_name = 'infografia'

urlpatterns = [
    path('', views.home, name='home'),
]
