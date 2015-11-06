from django import template

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
    return delta
