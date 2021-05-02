from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Initiative
from django.urls import reverse_lazy

# Create your views here.

class CreateInitiativeView(CreateView):
    model = Initiative
    fields = ['title', 'mission_description']
    template_name = 'initiatives/create_initiative.html'
    # TODO: change to correct url
    success_url = reverse_lazy('initiativedirectory')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()
        return super().form_valid(form)


def initiative_directory(request):
    initiatives = Initiative.objects.all()
    return render(request, 'initiatives/initiative_directory.html', {'initiatives': initiatives})
