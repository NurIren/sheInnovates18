from django.shortcuts import render
from django.http import HttpResponse

def index(request):

		return render(request, 'webapp/template.html')

def index1(request):

		return render(request, 'webapp/camera.html')

def index2(request):

		return render(request, 'webapp/t2page.html')