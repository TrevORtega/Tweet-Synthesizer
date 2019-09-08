from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandleForm

from markov.scraper2.markovey import *


def index(request):
    render (request, 'index.html')
    
    if request.method == 'POST':
    
        form = HandleForm(request.POST)
        if form.is_valid():
            #get the twitter handle from user
            handle = form.cleaned_data['handle']
            
            
            
            tweet = main(handle)
            
            results_redirect(request)
            
            
    
            return render(request, 'results.html', {'newTweet' : tweet, 'user' : handle})
    else:
        form = HandleForm()
        
    return render(request, 'index.html', {'form': form})
    

def results_redirect(request):
    
    return redirect('results/')
    