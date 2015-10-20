# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('general', models.BooleanField()),
                ('active', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('create_date', models.DateField()),
                ('image', models.FileField(upload_to=b'project_images/')),
                ('creator', models.ForeignKey(related_name='project_creator', to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('create_date', models.DateField()),
                ('due_date', models.DateField()),
                ('assigned_to', models.ForeignKey(related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(related_name='task_creator', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='WebServices.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('repeat_period_in_hour', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('hours_to_remain_on_board', models.IntegerField()),
                ('number_restriction', models.IntegerField()),
                ('task_message', models.TextField()),
                ('num_of_episodes', models.IntegerField()),
                ('target', models.IntegerField()),
                ('todo_num', models.IntegerField()),
                ('parent_type', models.IntegerField()),
                ('num_of_repeat', models.IntegerField()),
                ('public_user_task', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(to='WebServices.Type'),
        ),
    ]
