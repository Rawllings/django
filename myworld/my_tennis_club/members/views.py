from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Linus',
        'fruits': ["Apple", "Banana", "Cherry", "Orange"],
        'mymembers': mymembers,
        'greeting': 3,
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964'
            },
            {
                'brand': 'Ford',
                'model': 'Sierra',
                'year': '1941'
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970'
            },
            {
                'brand': 'Volvo',
                'model': 'XC90',
                'year': '2016'
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964'
            }
        ]
    }
    return HttpResponse(template.render(context, request))