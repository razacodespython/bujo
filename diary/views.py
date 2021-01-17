from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import bujodb
from .forms import bujoform

# Create your views here.

def home(request):
    bujo = bujodb.objects.all()
    monday = bujodb.objects.filter(day='M')
    tuesday = bujodb.objects.filter(day='T')
    wednesday = bujodb.objects.filter(day='W')
    thursday = bujodb.objects.filter(day='Th')
    friday = bujodb.objects.filter(day='F')
    saturday = bujodb.objects.filter(day='Sa')
    sunday = bujodb.objects.filter(day='Su')
    otherstuff = bujodb.objects.filter(day='X')


    return render(request, "home.html", {'bujo':bujo, 'monday':monday, 'tuesday':tuesday,
    'wednesday':wednesday, 'thursday':thursday, 'friday':friday, 'saturday':saturday, 'sunday':sunday, 'otherstuff':otherstuff})


def createpostmonday(request):
    bujo = bujodb.objects.all()
    form = bujoform()
    
    monday = bujodb.objects.filter(day='M')
    tuesday = bujodb.objects.filter(day='T')
    wednesday = bujodb.objects.filter(day='W')
    thursday = bujodb.objects.filter(day='Th')
    friday = bujodb.objects.filter(day='F')
    saturday = bujodb.objects.filter(day='Sa')
    sunday = bujodb.objects.filter(day='Su')
    otherstuff = bujodb.objects.filter(day='X')

    if request.method == "POST":
        
        form = bujoform(request.POST)
        if form.is_valid():
            monday.delete()

            post = form.save(commit=False)
            post.save()
            return redirect('home')

    else:
        form = bujoform()
    return render(request, "createpost.html", {'form':form, 'monday':monday, 'tuesday':tuesday,
    'wednesday':wednesday, 'thursday':thursday, 'friday':friday, 'saturday':saturday, 'sunday':sunday, 'otherstuff':otherstuff})

def createposttuesday(request):
    bujo = bujodb.objects.all()
    form = bujoform()
    monday = bujodb.objects.filter(day='M')
    tuesday = bujodb.objects.filter(day='T')
    wednesday = bujodb.objects.filter(day='W')
    thursday = bujodb.objects.filter(day='Th')
    friday = bujodb.objects.filter(day='F')
    saturday = bujodb.objects.filter(day='Sa')
    sunday = bujodb.objects.filter(day='Su')
    otherstuff = bujodb.objects.filter(day='X')

    if request.method == "POST":
        
        form = bujoform(request.POST)
        if form.is_valid():
            tuesday.delete()

            post = form.save(commit=False)
            post.save()
            return redirect('home')

    else:
        form = bujoform()


    # if request.method =='POST':
    #     form = bujoform(request.POST)
    #     if form.is_valid():
    #         if form.fields['day'] == 'M':
    #             monday.delete()
    #             post = form.save(commit=False)
    #             post.save()
    #         elif form.fields['day'] == 'T':
    #             tuesday.delete()
    #             post = form.save()
    #             post.save()
    #         return redirect('home')
    #     else:
    #         form = bujoform()

    return render(request, "createposttuesday.html", {'form':form, 'monday':monday, 'tuesday':tuesday,
    'wednesday':wednesday, 'thursday':thursday, 'friday':friday, 'saturday':saturday, 'sunday':sunday, 'otherstuff':otherstuff})