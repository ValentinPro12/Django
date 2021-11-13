from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


class IsExecutor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class TatyList(generics.ListAPIView):
    queryset = Taty.objects.all()
    serializer_class = TatySerializer


class TatyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Taty.objects.all()
    serializer_class = TatySerializer
    permission_classes = (IsExecutor,)


class TatyCreateView(generics.CreateAPIView):
    queryset = Taty.objects.all()
    serializer_class = CreateTatySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
