from django.shortcuts import render

# Create your views here.

def main_landing(request):
    return render(request, 'info_landing.html', {})
