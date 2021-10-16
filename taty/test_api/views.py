from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class TatyList(generics.ListAPIView):
    queryset = Taty.objects.all()
    serializer_class = TatySerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer