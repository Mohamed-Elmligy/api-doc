from rest_framework import serializers
from .models import Project, Api

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'        