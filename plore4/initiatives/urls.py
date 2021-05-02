from django.urls import path

from . import views

urlpatterns = [
    path('create_initiative/', views.CreateInitiativeView.as_view(), name='newinitiative'),
    path('', views.initiative_directory, name='initiativedirectory'),
]