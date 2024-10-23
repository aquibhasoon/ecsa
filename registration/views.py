from django.shortcuts import render, redirect, HttpResponse
from .models import Application
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
	return render(request, 'registration/register.html')


@login_required()
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			application = form.save(commit=False)  # Don't save to DB yet
			application.student = request.user  # Set the current user as student
			application.save()  # Now save to DB
			return redirect('idcard')  # Redirect to a success page
	else:
		has_application = Application.objects.filter(student=request.user).exists()
		if not has_application:
			form = RegistrationForm()
		else:
			return redirect('idcard')

	context = {"form": form}
	return render(request, 'registration/register.html', context)


def idcard(request):
	context = {"id_card": Application.objects.filter(student_id_no=22021894).last(),

	           }
	print(context)
	return render(request, 'registration/idcard.html', context)



