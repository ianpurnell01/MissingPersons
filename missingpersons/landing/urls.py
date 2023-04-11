from django.urls import path
from .views import indexPageView, databasePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path('database/', databasePageView, name='database')
]
