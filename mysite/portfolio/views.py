from django.shortcuts import render

# Create your views here.
def basic_web(request):
    return render(request, 'portfolio/index.html', {})
