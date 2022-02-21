from django.shortcuts import render
from django.http import HttpResponse


# import model


def index(request):

    context_dict = {'boldmessage': 'here is the index page'}
    
    return render(request, 'project/index.html', context=context_dict)



def forum(request):
    return render(request, 'project/forum.html', context={})


def about(request):
    return render(request, 'project/about.html', context={})
