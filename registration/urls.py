from django.contrib import admin
from django.urls import path
from .views import home, idcard

urlpatterns = [
	path('', home, name='home'),
	path('idcard', idcard, name='idcard'),
]
