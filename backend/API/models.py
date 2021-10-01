from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import DiscordUserOauth2Manager


# Create your models here.

class DiscordUser(models.Model):
    objects = DiscordUserOauth2Manager()
    id = models.CharField(primary_key=True, max_length=100)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100, null=True)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)
    REQUIRED_FIELDS = ['discord_tag', 'avatar', 'public_flags', 'flags', 'locale', 'mfa_enabled']
    USERNAME_FIELD = 'id'

    is_anonymous = False

    is_authenticated = True

    is_active = True

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class FormCreate(models.Model):
    form_id = models.AutoField(primary_key=True)
    serverid = models.BigIntegerField()
    userid = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    Formfields = models.JSONField()
    FormName = models.CharField(max_length=200)

    def __str__(self):
        return self.FormName


class FormResponse(models.Model):
    id = models.AutoField(primary_key=True)
    form_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    Response = models.JSONField()


class LoginTable(models.Model):
    loggedIn = models.BooleanField()
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)


class AccessTokenTable(models.Model):
    access_token = models.CharField(max_length=200)
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)


class UserServers(models.Model):
    servers = models.JSONField()
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
