from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:q_id>/', views.detail, name='detail'),
    path('<int:q_id>/results/', views.results, name='results'),
    path('<int:q_id>/results/vote/', views.vote, name='vote'),
]