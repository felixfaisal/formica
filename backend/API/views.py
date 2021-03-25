from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from .serializer import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response 


redirect_url_discord = "https://discord.com/api/oauth2/authorize?client_id=728306573696303135&redirect_uri=localhost%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"
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


def discord_login(request): 
    return redirect(redirect_url_discord)

@api_view(["GET"])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def taskdetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def listcreate(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return(serializer.data)

@api_view(["POST"])
def listupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE", "GET"])
def listdelete(request, pk): 
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Succesfully Deleted")