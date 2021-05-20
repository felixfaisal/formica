import os
import environ
import requests
from dotenv import load_dotenv

from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

from rest_framework.authtoken.models import Token

from .models import FormCreate, FormResponse, LoginTable, AccessTokenTable, UserServers

load_dotenv()

redirect_url_discord = "https://discord.com/api/oauth2/authorize?client_id=728306573696303135&permissions=68608&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect%2F&response_type=code&scope=identify%20guilds%20bot"


def getServerChannels(access_token, serverid):
    print('Reached API query function')
    discord_url = "https://discord.com/api/v6/guilds/"+serverid+"/channels"
    response = requests.get(discord_url, headers={
        'Authorization': 'Bearer %s' % access_token
    })
    channels = response.json()
    return channels


def getUserServers(access_token):
    print('Reached to API query')
    response = requests.get("https://discord.com/api/v6/users/@me/guilds", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    servers = response.json()
    print(servers)
    return servers


def getUserInformation(access_token):
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    user = response.json()
    return user


def getAccessToken(code):
    data = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect/",
        "scope": "identify"
    }
    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }
    response = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers)
    # print(response.json())
    credentials = response.json()
    print(credentials)
    access_token = credentials['access_token']
    return access_token
