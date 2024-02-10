from django.shortcuts import render
from django.http import JsonResponse
from .serializers import Dota2TeamsSerializer, PersonSerializer
from .models import Dota2Teams, Person
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getTeam(request):
    team = Dota2Teams.objects.all()
    if request.method == 'GET':
        serializer = Dota2TeamsSerializer(team ,many=True)
        return JsonResponse({ "Teams" : serializer.data}, safe = False) 
    
@api_view(['POST'])
def addPerson(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'main/index.html')
        return JsonResponse(serializer.errors, status=400)
    
@api_view(['POST'])
def addTeam(request):
    if request.method == 'POST':
        serializer = Dota2TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'main/index.html')
        return JsonResponse(serializer.errors, status=400)
    