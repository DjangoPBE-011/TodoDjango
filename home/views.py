from django.shortcuts import render
import random

def homeview(request):
    return render(request, 'index.html')

def randomson(request):
    number = random.randint(1, 100) 
    context = {
        "number": number,
        "text": "Salom Jamshidbek 😎"
    }
    return render(request, template_name="random.html", context = context)