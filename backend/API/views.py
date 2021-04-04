from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
# Create your views here.
from .serializer import FormCreateSerializer, FormResponseSerializer, DiscordUserSerializer
from .models import FormCreate, FormResponse, LoginTable
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
import requests
import environ 
from dotenv import load_dotenv
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
from rest_framework.authtoken.models import Token
load_dotenv()


redirect_url_discord = "https://discord.com/api/oauth2/authorize?client_id=728306573696303135&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect%2F&response_type=code&scope=identify"

@login_required(login_url='login/')
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def index(request):
    #token = Token.objects.get(user_id=request.user.id)
    print(request.user)
    #print(request.user)
    #return Response(serializer.data)
    return JsonResponse("Have false", safe=False)


def discord_login(request): 
    return redirect(redirect_url_discord)

def discord_logout(request):
    logout(request)
    return JsonResponse("Succesfully Logged out", safe=False)

def discord_login_redirect(request):
    code = request.GET.get('code')
    user = exchange_code(code)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    login(request, discord_user)
    print(request.user)
    token = Token.objects.get(user_id=discord_user)
    print(token.key)
    return JsonResponse(token.key, safe=False)



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def formlist(request):
    if request.user:
        #forms = FormCreate.objects.filter(userid=request.user)
        forms = FormCreate.objects.all()
        serializer = FormCreateSerializer(forms, many=True)

        return Response(serializer.data)
        
    return Response("You are not logged in!")

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def responselist(request):
    print(request.user)
    response = FormResponse.objects.all()
    serializer = FormResponseSerializer(response, many=True)
    return Response(serializer.data)

@login_required(login_url='login/')
@api_view(["GET"])
def formresponse(request, FormName):
    form = FormCreate.objects.get(FormName=FormName, userid=request.user)
    response = FormResponse.objects.filter(form=form)
    serializer = FormResponseSerializer(response, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def formcreateresponse(request):
    serializer = FormCreateSerializer(data=request.data)
    
    if serializer.is_valid():
       form = serializer.data 
       form["userid"] = request.user
       newform = FormCreate()
       newform.id = form['id']
       newform.userid = form['userid']
       newform.FormName = form['FormName']
       newform.Formfields = form['Formfields']
       print(newform)
       newform.save()
    
    return Response(serializer.data)


@api_view(['GET','POST'])
def userCreate(request):
    access_token = request.data.get('access_token')
    user = getUserInformation(access_token)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    #login(request, discord_user)
    #print(request.user)
    token = Token.objects.get(user_id=discord_user)
    print(token.key)
    return Response(token.key)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
def userLogin(request): 
    login = LoginTable.objects.get(user=request.user)
    return JsonResponse(login.loggedIn, safe=False)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def userLogout(request):
    login = LoginTable.objects.get(user=request.user)
    return JsonResponse('False', safe=False)
    


def getUserInformation(access_token):
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    user = response.json()
    return user


def exchange_code(code):
    data = {
        "client_id":os.getenv("CLIENT_ID"),
        "client_secret":os.getenv("CLIENT_SECRET"),
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect/", 
        "scope": "identify"
    }
    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    #print(response.json())
    credentials = response.json()
    print('Access token')
    access_token = credentials['access_token']
    print(access_token)
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    user = response.json()
    return user

