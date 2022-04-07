from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def loginView(request):
    return render(request, 'account/login/index.html')


def authentication(request):
    # return HttpResponse('authentication')
    user = authenticate(username='admin', password='password')
    if user is not None:
        login(request, user)
        return HttpResponse('logged in')
    else:
        return HttpResponse('not logged in')
