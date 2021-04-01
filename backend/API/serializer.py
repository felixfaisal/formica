from rest_framework import serializers
from .models import Task, FormCreate

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class FormCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCreate 
        fields = ['id','Formfields','FormName']