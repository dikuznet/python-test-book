from django.http import HttpResponse
from django.shortcuts import render
from .models import Demo
from django.db import transaction

def first_insert():
    Demo.objects.create()
    raise Exception("FUCK")

def second_insert():
    Demo.objects.create()

# @transaction.atomic
def home(_):
    first_insert()
    second_insert()
    return HttpResponse("ok")
# Create your views here.
