from django.shortcuts import render
from .models import Person

# Create your views here.
def indexPageView (request) :
    return render(request, 'landing/index.html')

def databasePageView (request) :
    people = Person.objects.all()

    context = {
        'data' : people
    }

    return render(request, 'landing/database.html', context)

def resourcePageView (request) :
    return render(request, 'landing/resources.html')

def individualPageView (request, id) :
    missingIndividual = Person.objects.get(id=id)

    context = {
        'data' : missingIndividual
    }

    return render (request, 'landing/individual.html', context)
