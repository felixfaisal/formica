from rest_framework import serializers
from .models import  FormCreate, FormResponse, DiscordUser, UserServers


class FormCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCreate 
        fields = ['Formfields','FormName','serverid']

class FormBotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCreate
        fields = ['form_id','Formfields','FormName','serverid']

class FormResponseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FormResponse
        fields = ['form','user_id', 'Response']

class FormBotResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponse
        fields = ['Response', 'user_id']

class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ['discord_tag', 'avatar']

class UserServersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserServers
        fields = ['servers']