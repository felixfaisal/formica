from django.db import models
from .managers import DiscordUserOauth2Manager
from django_mysql.models import JSONField

# Create your models here.

class DiscordUser(models.Model):
    objects = DiscordUserOauth2Manager()
    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self, request): 
        return True
    
    def is_active(self, request):
        return True

class FormCreate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    Formfields = models.JSONField()
    FormName = models.CharField(max_length=200)

    def __str__(self):
        return self.FormName

class FormResponse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    form = models.ForeignKey(FormCreate, on_delete=models.CASCADE)
    responseid = models.BigIntegerField()
    response = models.JSONField()