from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTeam, name='getTeam'), # This will match the root URL
    path('addPerson/', views.addPerson, name='addPerson'), # This will match the /addPerson/ URL
    path('addTeam/', views.addTeam, name='addTeam'), # This will match the /addTeam/ URL
]