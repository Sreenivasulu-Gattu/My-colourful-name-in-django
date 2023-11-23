from django.shortcuts import render

# Create your views here.
def myName(request):
    return render(request,'My name Colourful.html')