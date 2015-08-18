from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .forms import UserRegistrationForm, UserForm
from .models import UserRegistration

# Create your views here.


def index(request):
    return render_to_response('Tunda/index.html', {}, RequestContext(request))


def sign_up(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile = UserRegistrationForm(request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            userp = UserRegistration(user=user, City=user_profile.cleaned_data['city'],
                                     Address=user_profile.cleaned_data['address'])
            # userp = user_profile.save(commit=False)

            # userp.user = user
            userp.save()
            return render_to_response('Tunda/index.html', {}, RequestContext(request))
        else:
            print user_form.errors, user_profile.errors
    else:
        user_form = UserForm()
        user_profile = UserRegistrationForm()
        return render(request, 'Tunda/signUp.html', {'user_form': user_form, 'user_profile': user_profile})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect('/Tunda/index/')

                return render_to_response('Tunda/index.html', {}, RequestContext(request))
            else:
                return HttpResponse('your account is disabled')
        else:
            return HttpResponse('Invalid login details provided ')
    else:
        return render(request, 'Tunda/signUp.html', {})


@login_required
def user_logout(request):
    logout(request)
    return render_to_response('Tunda/index.html', {}, RequestContext(request))


def products(request):
    return render(request, 'Tunda/products.html', {})




