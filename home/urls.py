from django.urls import path
from .views import home, login

urlpatterns = [
	
	path('', login, name='login'),

]
