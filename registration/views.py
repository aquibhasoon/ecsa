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
    application = Application.objects.filter(student=request.user, accepted=True).last()

    if application:
        context = {"id_card": application}
    else:
        context = {"message": "Your application is not verified yet. Please wait for approval."}

    return render(request, 'registration/idcard.html', context)



