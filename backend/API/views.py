from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .serializer import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(["GET"])
def index(request):
    api_urls = {
        "List":"/list/",
        "Detail View":"/list-detail/<str:pk>/",
        "Create":"/list-create/",
        "Update":"/list-update/<str:pk>/",
        "Delete":"/list-delete/<str:pk>/"
    }
    return Response(api_urls)

@api_view(["GET"])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def listcreate(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return(serializer.data)