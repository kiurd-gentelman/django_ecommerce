from django.shortcuts import render

from team import models
from .models import About
from team.models import Team


# Create your views here.

def index(request):
    about = About.objects.first()
    teams = Team.objects.all()
    return render(request, 'about/index.html', {'about': about, 'teams': teams})
