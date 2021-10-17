from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.views import APIView

from .models import *
from .serializers import *


# TODO все это надо переделать на абстрактный класс, на надо будет казывать только название класса
# Create your views here.
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class TatyList(generics.ListAPIView):
    queryset = Taty.objects.all()
    serializer_class = TatySerializer



# TODO обновление записи, пока не понял как это работает

class TatyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Taty.objects.all
    serializer_class = TatySerializer


# TODO тут ошибка, что то не так с URLS надо разобраться
class TatyCreateView(generics.UpdateAPIView):
    queryset = Taty.objects.all
    serializer_class = CreateTatySerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
