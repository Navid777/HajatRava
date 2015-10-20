from django.contrib.auth.models import User
from django.db import models


class Type(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    repeat_period_in_hour = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    hours_to_remain_on_board = models.IntegerField(null=True, blank=True)
    number_restriction = models.IntegerField(null=True, blank=True)
    task_message = models.TextField(null=True, blank=True)
    num_of_episodes = models.IntegerField(null=True, blank=True)
    target = models.IntegerField(null=True, blank=True)
    todo_num = models.IntegerField(null=True, blank=True)
    parent_type = models.IntegerField(null=True, blank=True)
    num_of_repeat = models.IntegerField(null=True, blank=True)
    public_user_task = models.TextField(null=True, blank=True)


class Project(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    general = models.BooleanField(blank=True)
    active = models.BooleanField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, related_name='project_creator', null=True, blank=True)
    type = models.ForeignKey(Type, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='member')
    image = models.FileField(upload_to='project_images/', null=True, blank=True)


class Task(models.Model):
    title = models.TextField(null=True, blank=True)
    done = models.BooleanField(blank=True, default=False)
    project = models.ForeignKey(Project, null=True, blank=True)
    create_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, related_name="assigned_to", null=True, blank=True)
    creator = models.ForeignKey(User, related_name="task_creator", null=True, blank=True)


class Text(models.Model):
    TITLE_CHOICES = (('TI', 'title'), ('AD', 'advertisement'))
    title = models.TextField(choices=TITLE_CHOICES)
    text = models.TextField()
