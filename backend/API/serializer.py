from rest_framework import serializers
from .models import Task, FormCreate, FormResponse

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class FormCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCreate 
        fields = ['id','Formfields','FormName']

class FormResponseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FormResponse
        fields = ['id','responseid', 'response']