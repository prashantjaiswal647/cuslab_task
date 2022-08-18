from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('', home),
    path('get-destination/<id>/' , get_destination),
    path('account/' , AccountAPI.as_view()),
    path('destination/' , DestinationAPI.as_view()),
    path('register/' , RegisterUser.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]