from django.shortcuts import render


# Create your views here.
def indexPageView (request) :
    return render(request, 'landing/index.html')

def databasePageView (request) :
    return render(request, 'landing/database.html')

