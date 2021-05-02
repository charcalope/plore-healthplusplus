from django.urls import path

from . import views

urlpatterns = [
    path('identify/', views.mu_identify_view, name='identify'),
    path('annotate/', views.mu_annotate, name='annotate'),
    path('summarize/', views.mu_summarize, name='summarize'),
    path('profilex/', views.mu_profile, name='profilex'),
]