from django import template
from film.models import *
from film.forms import *

register = template.Library()
@ register.simple_tag()
def newest(cnt = 3):
    return film.objects.order_by("-time_add")[:cnt]

@ register.simple_tag()
def genres():
    return Genre.objects.all()

@register.simple_tag()
def random():
    return film.objects.order_by('?')[:4]

@register.simple_tag()
def login():
    return LoginUser()

@register.simple_tag()
def country():
    return Country.objects.all()

@register.simple_tag()
def age_rating():
    return AgeRating.objects.all()