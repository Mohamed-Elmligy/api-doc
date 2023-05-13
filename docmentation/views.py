from django.shortcuts import render
from .models import Api, Project

from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from .serializers import ProjectSerializer, ApiSerializer

from django.http import Http404

# Create your views here.

# project model
@api_view(['GET','POST'])
def Projects(request):
    # GET
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ProjectSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
#3.1 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def Project_pk(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        project.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)    
    
# api model methods
@api_view(['GET', 'POST'])
def api(request):
    # GET
    if request.method == 'GET':
        api = Api.objects.all()
        serializer = ApiSerializer(api, many=True)
        return Response(serializer.data)  
    # POST  
    elif request.method == 'POST':
        serializer = ApiSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def api_pk(request, pk):
    try:
        api = Api.objects.filter(project= pk)
    except Project.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ApiSerializer(api, many=True)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = ApiSerializer(api, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        api.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)        
    