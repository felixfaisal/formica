from rest_framework import serializers
from .models import  FormCreate, FormResponse, DiscordUser, UserServers


class FormCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCreate 
        fields = ['id','Formfields','FormName']

class FormResponseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FormResponse
        fields = ['id','responseid', 'response']

class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ['discord_tag', 'avatar']

class UserServersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserServers
        fields = ['servers']