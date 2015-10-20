# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('WebServices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(choices=[(b'TI', b'title'), (b'AD', b'advertisement')])),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='member',
            new_name='members',
        ),
        migrations.AlterField(
            model_name='project',
            name='create_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(related_name='project_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(null=True, upload_to=b'project_images/', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.ForeignKey(blank=True, to='WebServices.Type', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(related_name='assigned_to', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(related_name='task_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, to='WebServices.Project', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='hours_to_remain_on_board',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='num_of_episodes',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='num_of_repeat',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='number_restriction',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='parent_type',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='public_user_task',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='repeat_period_in_hour',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='target',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='task_message',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='title',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='todo_num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
