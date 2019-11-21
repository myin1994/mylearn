from django.shortcuts import render,HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    print('app02',reverse('app02:index'))
    return HttpResponse('app02index')