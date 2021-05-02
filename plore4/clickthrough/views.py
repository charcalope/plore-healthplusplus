from django.shortcuts import render

# Create your views here.
def mu_identify_view(request):
    return render(request, 'mockup/mu_identify.html', {})

def mu_annotate(request):
    return render(request, 'mockup/mu_annotate.html', {})

def mu_summarize(request):
    return render(request, 'mockup/mu_summarize.html', {})

def mu_profile(request):
    return render(request, 'mockup/mu_public_profile.html', {})