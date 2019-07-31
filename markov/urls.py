from django.urls import path

from . import views

from django.views.generic import TemplateView

from .views import results_redirect

urlpatterns = [
	path('', views.index, name='index'),
    
    path('results/', views.results_redirect), 
]