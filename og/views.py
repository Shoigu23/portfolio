from django.shortcuts import render
from og.models import Skill, Message, Project
from django.http import HttpResponseRedirect


# Create your views here.


def og(request):
    # skils = Skill.objects.get(title = 'Python')
    # skils = Skill.objects.filter(title = 'Python')
    # skils = Skill.objects.first()
    # skils = Skill.objects.last()
    skill = Skill.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html', 
    {'skill': skill, 'project': project})

def message(request):
    if request.method == 'POST':
        message = Message()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.text = request.POST.get('message')
        message.save()
    return HttpResponseRedirect('/')
