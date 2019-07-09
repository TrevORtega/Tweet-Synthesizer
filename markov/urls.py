from django.urls import path

from . import views

from django.views.generic import TemplateView

from .views import results_redirect

urlpatterns = [
	path('', views.index, name='index'),
    
    path('results/', views.results_redirect), 
    
    #path('?name=<int:handle>/&page=<int:pages>/', views.handle, name='handle', views.pages, name='pages'),
	
	# path('<int:question_id>/', views.handle, name='handle'),
	
	#path('<int:question_id>/', views.detail, name='detail'),
	
	#path('<int:question_id>/results/', views.results, name='results'),
	
	#path('<int:question_id>/vote/', views.vote, name='vote'),

]