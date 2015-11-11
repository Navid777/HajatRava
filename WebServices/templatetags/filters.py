#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.utils.encoding import smart_text, force_text

__author__ = 'navid'

register = template.Library()

@register.filter(name='android')
def android(delta):
    if delta is None:
        return 'null'
    if delta == 'None':
        return 'null'
    if delta == None:
        return 'null'
    if delta is True:
        return 'true'
    if delta is False:
        return 'false'
    if delta == '':
        return 'null'
    if isinstance(delta, (int, long, float)):
        return delta
    return "\""+delta+"\""


@register.filter(name='public_user_task')
def public_user_task(obj):
    return force_text(obj.public_user_task).replace("%s", str(obj.get_episode()))

@register.filter(name="title")
def title(obj):
    return force_text(obj.title).replace("%s", str(obj.project.type.get_episode()))
