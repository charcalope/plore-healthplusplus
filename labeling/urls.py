from django.urls import path

from . import views

urlpatterns = [
    path('', views.basic_index_test, name='index'),
    path('allconditions/', views.view_all_conditions, name='allconditions'),
    path('newcondition/', views.CreateConditionView.as_view(), name='newcondition'),
    path('testpanel/', views.test_panel_view, name='testpanel'),
    path('newconditionmeta/', views.CreateConditionMetaView.as_view(), name='newconditionmeta'),
    path('allconditionmetas/', views.view_all_condition_metas, name='allconditionmetas'),
]