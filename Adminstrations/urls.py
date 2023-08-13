from django.urls import path
from . import views

app_name = 'administrations'

urlpatterns = [
    path('', views.basic_view, name='basic'),
]