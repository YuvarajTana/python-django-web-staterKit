from bookmark import settings
import requests
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError

from django.shortcuts import render

@csrf_exempt
def index(request):
	response = render(request,'index.html')
	return response