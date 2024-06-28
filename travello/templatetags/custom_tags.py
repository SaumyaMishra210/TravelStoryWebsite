from django import  template

register = template.Library()

from ..models import CustomTags

@register.simple_tag
def fun():
    return CustomTags.objects.count()

@register.inclusion_tag('greetings.html',takes_context= True)
def fun_inclusion(context):
    user = context['user']
    return  {'user':user}