from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    helpdict = {'help': 'HELP PAGE'}
    return render(request, 'second_app/help.html', context=helpdict)