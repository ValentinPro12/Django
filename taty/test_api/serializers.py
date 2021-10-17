from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'first_name', 'last_name']


class TatySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    taty_type = serializers.CharField(source='get_taty_type_display')

    class Meta:
        model = Taty
        fields = '__all__'


class CreateTatySerializer(serializers.ModelSerializer):

    class Meta:
        model = Taty
        fields = '__all__'
