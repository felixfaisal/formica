from rest_framework import serializers

from .models import FormCreate, FormResponse, DiscordUser, UserServers

''' We are use different serializers for similar models so that it can be utilized in different API routes '''


class FormCreateSerializer(serializers.ModelSerializer):  # api/form/list
    class Meta:
        model = FormCreate
        fields = ['Formfields', 'FormName', 'serverid']


class FormBotCreateSerializer(serializers.ModelSerializer):  # api/bot/forms/<str:serverid>
    class Meta:
        model = FormCreate
        fields = ['form_id', 'Formfields', 'FormName', 'serverid']


class FormResponseSerializer(serializers.ModelSerializer):  # api/responses/, api/form/response/<str:FormName>, api/bot/form/response/<str:FormName> # NOQA
    class Meta:
        model = FormResponse
        fields = ['form_id', 'user_id', 'Response']


class FormBotResponseSerializer(serializers.ModelSerializer):  # api/bot/response/
    class Meta:
        model = FormResponse
        fields = ['form_id', 'Response', 'user_id']


class UserResponseSerializer(serializers.ModelSerializer):  # api/user/responses
    class Meta:
        model = FormResponse
        fields = ['id', 'form', 'user_id', 'Response']


class DiscordUserSerializer(serializers.ModelSerializer):  # api/user/information
    class Meta:
        model = DiscordUser
        fields = ['discord_tag', 'avatar']


class UserServersSerializer(serializers.ModelSerializer):  # Not Found // Deprecatted Serializer
    class Meta:
        model = UserServers
        fields = ['servers']
