from django.urls import path
from . import views

urlpatterns = [
    path('', views.plot_graph, name='plot_graph'),
]
