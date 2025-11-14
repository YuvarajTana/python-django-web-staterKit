from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Main index view for the bookmark application.
    Renders the home page with the TODO interface.
    """
    return render(request, 'index.html')
