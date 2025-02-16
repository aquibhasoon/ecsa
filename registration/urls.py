from django.contrib import admin
from django.urls import path
from .views import idcard, register,disclaimer

urlpatterns = [
	path('', register, name='register'),
	path('idcard/', idcard, name='idcard'),
    path('disclaimer/', disclaimer, name='disclaimer'),

]
