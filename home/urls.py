from django.urls import path
from home.views import homeview,randomson

urlpatterns = [
    path('',homeview,name='home'),
    path('random/',randomson,name='randomson')
]