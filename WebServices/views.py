from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from WebServices.models import Text, Task, Project


def get_about_us(request):
    text = Text.objects.get(title="AU")
    return render(request, 'about_us.html', {'text': text.text})


def get_ad_message(request):
    text = Text.objects.get(title="AD")
    return render(request, 'ad_message.html', {'text': text.text})


def set_task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = True
    task.save()
    return render(request, 'json/success.json', {'task': task})


def get_projects(request):
    projects = Project.objects.all()
    return render(request, 'json/projects.json', {'projects': projects})


def get_user_projects(request, user_id):
    projects = Project.objects.filter(member__id=user_id)
    return render(request, 'json/projects.json', {'projects': projects})


def get_user_tasks(request, user_id):
    tasks = Task.objects.filter(assigned_to__id=user_id)
    return render(request, 'json/tasks.json', {'tasks': tasks})


def add_user_to_project(request, project_id, user_id):
    user = User.objects.filter(id=user_id)
    project = Project.objects.get(id=project_id)
    project.members.add(user)
    project.save()
    return render(request, 'json/success.json', {'project': project})


def get_project_tasks(request, project_id):
    tasks = Task.objects.filter(project__id=project_id)
    return render(request, 'json/tasks.json', {'tasks': tasks})


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        if len(User.objects.filter(username=username)) == 0:
            return HttpResponse("F1")
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active():
                login(request, user)
                return HttpResponse("S")
        return HttpResponse("F2")


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'json/success.json')
