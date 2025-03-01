from django.urls import path
from . import views

# URL CONFIGS WE MADE
urlpatterns = [
   #path('url/route', view function) this is below
    path('hello/', views.say_hello)
]