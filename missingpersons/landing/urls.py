from django.urls import path
from .views import indexPageView, databasePageView, resourcePageView, individualPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('database/', databasePageView, name='database'),
    path('resources/', resourcePageView, name='resources'),
    path('<int:id>/', individualPageView, name = 'individual'),
]
