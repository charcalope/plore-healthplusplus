from django.shortcuts import render, HttpResponse
from .models import ConditionMeta, Condition, Article
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def condition_dashboard(request, condition_id):
    return render(request, 'anndash/condition_dash.html', {})

def basic_index_test(request):
    return HttpResponse('labeling app')

def test_panel_view(request):
    return render(request, 'anndash/test_panel.html', {})

def view_all_conditions(request):
    conditions = Condition.objects.all()
    return render(request, 'anndash/view_conditions.html', {'conditions': conditions})

class CreateConditionView(CreateView):
    model = Condition
    fields = ['title']
    template_name = 'anndash/new_condition.html'
    success_url = reverse_lazy('allconditions')

class CreateConditionMetaView(CreateView):
    model = ConditionMeta
    fields = ['condition']
    template_name = 'anndash/new_condition_meta.html'
    success_url = reverse_lazy('allconditionmetas')

def view_all_condition_metas(request):
    condition_metas = ConditionMeta.objects.all()
    return render(request, 'anndash/all_condition_metas.html', {'condition_metas': condition_metas})
