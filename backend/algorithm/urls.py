from django.contrib import admin
from django.urls import include, path
from .views import PathAPIView

urlpatterns = [
    path('', PathAPIView.as_view(), name='path')
]
