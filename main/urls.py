from main.views import process_data_ninja
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process_data_dojo', views.process_data_dojo),
    path('process_data_ninja', views.process_data_ninja),
]