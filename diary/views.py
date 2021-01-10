from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import bujodb
from .forms import bujoform

# Create your views here.

def home(request):
    bujo = bujodb.objects.all()
    return render(request, "home.html", {'bujo':bujo})


def createpost(request):
    bujo = bujodb.objects.all()
    form = bujoform

    if request.method =='POST':
        form = bujoform(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = bujoform()

    return render(request, "createpost.html", {'form':form})