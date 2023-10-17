from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics

# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
