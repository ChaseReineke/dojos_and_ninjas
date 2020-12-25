from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo, Ninja
def index(request):
    context = {
    	"all_the_dojos": Dojo.objects.all(),
        "all_the_ninjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def process_data_dojo(request):
    new_dojo = Dojo.objects.create(
    name = request.POST['name'],
    city = request.POST['city'],
    state = request.POST['state'],)
    new_dojo.save()
    return redirect('/')

def process_data_ninja(request):
    new_ninja = Ninja.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    location = Dojo.objects.get(id=request.POST['dojo']),)
    new_ninja.save()
    return redirect('/')