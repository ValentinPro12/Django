from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('tatys/all', TatyList.as_view()),
    path('tatyupdate/<int:pk>', TatyRetrieveUpdateView.as_view()),
    path('taty/new', TatyCreateView.as_view()),
    # path('taty/<int:pk>/', TatyCreateView.as_view()),
    path('users/all', UserList.as_view()),
]
