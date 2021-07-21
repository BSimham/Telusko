from django.shortcuts import render
from django.http import HttpResponse
from .models import items
# Create your views here.
def index(request):
    its=items.objects.all()
    return render(request,'index.html',{'its':its})