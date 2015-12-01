#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.encoding import force_text
from django.views.decorators.csrf import csrf_exempt
from WebServices.models import Text, Task, Project
from django.contrib.auth import login as auth_login
import datetime


def get_about_us(request):
    text = Text.objects.get(title="AU")
    tasks = Task.objects.filter(done=True)
    salavat_num = 0
    quran_parts = 0
    fatehe_num = 0
    doa_num = 0
    for task in tasks:
        type = task.project.type.parent_type
        if type == 1:
            salavat_num += task.project.type.todo_num
        elif type == 2:
            quran_parts += task.project.type.todo_num
        elif type == 3:
            fatehe_num += task.project.type.todo_num
        else:
            doa_num += task.project.type.todo_num
    return render(request, 'about_us.html', {'text': text.text, 'salavat': salavat_num,
                                             'quran': quran_parts, 'fatehe': fatehe_num, 'doa': doa_num})


def get_ad_message(request):
    text = Text.objects.get(title="AD")
    return render(request, 'ad_message.html', {'text': text.text})


def set_task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = True
    task.save()
    return render(request, 'json/success.json', {'task': task})


def get_projects(request):
    projects = Project.objects.filter(active=True).order_by('-importance')
    return render(request, 'json/projects.json', {'projects': projects})


def get_user_projects(request, user_id):
    projects = Project.objects.filter(member__id=user_id).order_by('-importance')
    return render(request, 'json/projects.json', {'projects': projects})


def get_user_tasks(request, user_id):
    tasks = Task.objects.filter(assigned_to__id=user_id)
    return render(request, 'json/tasks.json', {'tasks': tasks})


def add_user_to_project(request, project_id, username):
    user = User.objects.get(username=username)
    project = Project.objects.get(id=project_id)
    project.members.add(user)
    project.save()
    task = Task.objects.create(project=project, assigned_to=user, creator=user, due_date=project.end_date,
                               create_date=datetime.date.today(), title=force_text(project.type.public_user_task).replace("%s", str(project.type.get_episode())))
    task.save()
    return render(request, 'json/success.json', {'project': project})


def get_project_tasks(request, project_id):
    tasks = Task.objects.filter(project__id=project_id)
    return render(request, 'json/tasks.json', {'tasks': tasks})


def get_user_tasks(request, username):
    user = get_object_or_404(User, username=username)
    tasks = Task.objects.filter(assigned_to=user, done=False)
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
            if user.is_active:
                auth_login(request, user)
                return HttpResponse("S")
        return HttpResponse("F2")


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            return HttpResponse("-Error: نام کاربری فرستاده نشده است.")
        if 'password' in request.POST:
            password = request.POST['password']
        else:
            password = ''
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            return HttpResponse("-Error: ایمیل فرستاده نشده است.")
        try:
            user = User.objects.get(username=username)
            return HttpResponse("-Error: نام کاربری تکراری است.")
        except ObjectDoesNotExist:
            user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'json/success.json')
    else:
        return HttpResponse("-Error: داده ها ارسال نشده.")


def records(request, username):
    try:
        user = User.objects.get(username=username)
    except Exception:
        return HttpResponse("لطفا ثبت نام کنید.")
    tasks = Task.objects.filter(assigned_to=user, done=True)
    salavat_num = 0
    quran_parts = 0
    fatehe_num = 0
    doa_num = 0
    for task in tasks:
        type = task.project.type.parent_type
        if type == 1:
            salavat_num += task.project.type.todo_num
        elif type == 2:
            quran_parts += task.project.type.todo_num
        elif type == 3:
            fatehe_num += task.project.type.todo_num
        else:
            doa_num += task.project.type.todo_num
    return render(request, 'records.html', {'salavat': salavat_num, 'quran': quran_parts, 'fatehe': fatehe_num, 'doa': doa_num})


def get_project_information(request, username, project_id):
    project = get_object_or_404(Project, id=project_id)
    done_tasks = Task.objects.filter(project=project, done=True)
    user = get_object_or_404(User, username=username)
    khatm = len(done_tasks)*project.type.todo_num/project.type.target
    remaining_tasks = project.type.target/project.type.todo_num - \
        (len(done_tasks) % (project.type.target/project.type.todo_num))
    participated = len(Task.objects.filter(project=project, assigned_to=user)) != 0
    has_remaining_task = (len(Task.objects.filter(project=project, assigned_to=user, done=False)) == 0)and participated
    return render(request, 'json/project_info.json', {'khatm': khatm, 'remaining_tasks': remaining_tasks,
                                                      'participated': participated,
                                                      'has_remaining_task': has_remaining_task,
                                                      'done_tasks': len(done_tasks),
                                                      'type': project.type.id})


def get_project_information_without_user(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    done_tasks = Task.objects.filter(project=project, done=True)
    khatm = len(done_tasks)*project.type.todo_num/project.type.target
    remaining_tasks = project.type.target/project.type.todo_num - \
        (len(done_tasks) % (project.type.target/project.type.todo_num))
    participated = False
    has_remaining_task = False
    return render(request, 'json/project_info.json', {'khatm': khatm, 'remaining_tasks': remaining_tasks,
                                                      'participated': participated,
                                                      'has_remaining_task': has_remaining_task,
                                                      'done_tasks': len(done_tasks), 'type': project.type.id})
