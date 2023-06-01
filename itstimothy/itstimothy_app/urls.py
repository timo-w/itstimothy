from django.urls import path
from itstimothy_app import views

app_name = 'itstimothy'

urlpatterns = [
    path('', views.index, name='index'),
]