from django.shortcuts import render
from .models import Application


# Create your views here.

def home(request):
	return render(request, 'registration/idcard.html')

def idcard(request):
	context = { "id_card" : Application.objects.filter(id_no=26101).last(),

	}
	print(context)
	return render(request, 'registration/idcard.html', context)
