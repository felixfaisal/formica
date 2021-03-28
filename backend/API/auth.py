from django.contrib.auth.backends import BaseBackend 
from .models import DiscordUser

class DiscordAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user):
        find_user = DiscordUser.objects.filter(id=user['id'])
        print("Reached auth")
        if len(find_user) == 0:
            print("User not found")