from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood,notifications,healthservices
from .forms import NewUserForm,notificationsForm
from django.db.models import Q
from django.contrib.auth.models import User
import datetime as datetime

# Create your views here.
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/accounts/login/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="django_registration/registration_form.html", context={"register_form":form})

def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'notifications.html', {"notifications":all_notifications})

@login_required(login_url='/accounts/login/')
def blog(request):
    current_user=request.user
    profile = Profile.objects.get(username=current_user)
    blogposts = BlogPost.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'blog.html', {"blogposts":blogposts})

@login_required(login_url='/accounts/login/')
def health(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'health.html', {"healthservices":healthservices})


