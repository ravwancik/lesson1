from django.urls import path

from .views import *


urlpatterns =[
    path('', index),
    path('garilla/', garilla),
    path('ravshan/', ravshan),
    path('flew/', flew),
    path('kola/', kola)
]