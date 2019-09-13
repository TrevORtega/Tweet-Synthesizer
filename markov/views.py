from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandleForm

from .tasks import scrape_and_bake 


def index(request):
    # Render the index page
    render (request, 'index.html')
    
    # Ensure the form method from index is POST
    if request.method == 'POST':
        
        # Get the form from index
        form = HandleForm(request.POST)
        if form.is_valid():
            #get the twitter handle from user
            handle = form.cleaned_data['handle']
            
            # Use Celery to scrape and make tweet in the background
            tweet = scrape_and_bake.delay(handle)
            
            # Redirect to the result page
            results_redirect(request)
            
            
            # Return the request and all of our information to the result page
            return render(request, 'results.html', {'newTweet' : tweet, 'user' : handle})
    else:
        form = HandleForm()
        
    return render(request, 'index.html', {'form': form})
    

def results_redirect(request):
    
    return redirect('results/')
    