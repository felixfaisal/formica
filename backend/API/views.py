import os
import environ
import requests
from dotenv import load_dotenv

from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .serializer import FormCreateSerializer, FormResponseSerializer, DiscordUserSerializer, FormBotResponseSerializer, FormBotCreateSerializer, UserResponseSerializer
from .models import FormCreate, FormResponse, LoginTable, AccessTokenTable
from .helper import getServerChannels, getUserServers, getUserInformation, getAccessToken

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

load_dotenv()

redirect_url_discord = "https://discord.com/api/oauth2/authorize?client_id=728306573696303135&permissions=68608&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect%2F&response_type=code&scope=identify%20guilds%20bot"

def discord_login(request):
    return redirect(redirect_url_discord)


def discord_logout(request):
    logout(request)
    return JsonResponse("Succesfully Logged out", safe=False)


def discord_login_redirect(request):
    code = request.GET.get('code')
    access_token = getAccessToken(code)
    user = getUserInformation(access_token)
    servers = getUserServers(access_token)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    serverinfo = UserServers(user=discord_user, servers=servers)
    serverinfo.save()
    login(request, discord_user)
    print(request.user)
    print('Access token on redirect')
    print(access_token)
    token = Token.objects.get(user_id=discord_user)
    try:
        atoken = AccessTokenTable.objects.get(user=discord_user)
    except Exception:
        print('Creating new access token')
        atoken = AccessTokenTable(user=discord_user, access_token=access_token)
        atoken.save()

    atoken.access_token = access_token
    atoken.save()
    print(token.key)
    #redirect_url_react = 'http://localhost:3000/dashboard?token='+token.key
    return redirect('http://localhost:3000?user='+str(token.key))


@login_required(login_url='login/')
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def index(request):
    print(request.user)
    return JsonResponse("Have false", safe=False)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def formlist(request):
    if request.user:
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


@api_view(["GET"])
def formresponse(request, FormName):
    form = FormCreate.objects.get(FormName=FormName, userid=request.user)
    response = FormResponse.objects.filter(form_id=form.form_id)
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
        newform.userid = form['userid']
        newform.FormName = form['FormName']
        newform.Formfields = form['Formfields']
        newform.serverid = form['serverid']
        print(newform)
        newform.save()

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def userCreate(request):
    access_token = request.data.get('access_token')
    user = getUserInformation(access_token)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    token = Token.objects.get(user_id=discord_user)
    print('Access token')
    print(access_token)
    atoken = AccessTokenTable(user=discord_user, access_token=access_token)
    atoken.save()


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def userLogin(request):
    login = LoginTable.objects.get(user=request.user)
    return JsonResponse(login.loggedIn, safe=False)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def userLogout(request):
    login = LoginTable.objects.get(user=request.user)
    return JsonResponse('False', safe=False)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def userInformation(request):
    serializer = DiscordUserSerializer(data=request.user, many=False)
    serializer.is_valid()
    jsondata = {
        "userid": request.user.id,
        "tag": request.user.discord_tag,
        "avatar": request.user.avatar,
        "flags": request.user.flags,
    }
    return JsonResponse(jsondata, safe=False)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def userServers(request):
    access_token = AccessTokenTable.objects.get(user=request.user).access_token
    servers = getUserServers(access_token)
    return Response(servers)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def userResponses(request):
    responses = FormResponse.objects.filter(user_id=request.user.id)
    serializer = UserResponseSerializer(responses, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def serverChannels(request, ServerID):
    access_token = AccessTokenTable.objects.get(user=request.user).access_token
    print(access_token)
    channels = getServerChannels(access_token, ServerID)
    return Response(channels)


@api_view(['GET', 'POST'])
def botFormList(request, serverid):
    forms = FormCreate.objects.filter(serverid=serverid)
    serializer = FormBotCreateSerializer(forms, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def botFormResponse(request):
    serializer = FormBotResponseSerializer(data=request.data, many=False)
    if serializer.is_valid():
        data = serializer.data
        print(serializer.data)
        newformresponse = FormResponse()
        newformresponse.form_id = data['form_id']
        newformresponse.Response = data['Response']
        newformresponse.user_id = data['user_id']
        newformresponse.save()
        print(newformresponse)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def botFormResponseList(request, FormName):
    form = FormCreate.objects.get(FormName=FormName)
    responses = FormResponse.objects.filter(form_id=form.form_id)
    serializer = FormResponseSerializer(responses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def dashboardInformation(request):
    forms = FormCreate.objects.filter(userid=request.user).count()
    responses = FormResponse.objects.filter(user_id=request.user.id).count()
    shared_servers = 5
    formJson = {
        "Forms Created": forms,
        "Total Responses": responses,
        "Shared Servers": shared_servers
    }
    return JsonResponse(formJson, safe=False)

