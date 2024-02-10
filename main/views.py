from django.shortcuts import render
import requests
from rest.settings import API_URL
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def index(request):
    if request.method == 'GET':
        response = requests.get(API_URL)
        data = response.json()
        return render(request, 'main/index.html', {'data': data})
    elif request.method == 'POST':
        if request.POST.get('first_name'):
            response = requests.post(API_URL + 'addPerson/', data=request.POST)
            return redirect('index')
        elif request.POST.get('team_name'):
            response = requests.post(API_URL + 'addTeam/', data=request.POST)
            return redirect('index')