from django.urls import path, include
from .views import *

urlpatterns = [
    path('tatys/all', TatyList.as_view()),
    path('users/all', UserList.as_view()),
]
