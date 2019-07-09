from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandleForm

from markov.scraper.markovey import *


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
    
"""def markovey(handle):
    import markovify
    
    from twitter_scraper import get_tweets

    numPages = 25;
    #user = input("Enter twitter handle: ")
    #numPages = input("Enter number of pages to read (Max is 25): ")

    #numPages = int(numPages)

    tweets = '\n'.join([t['text'] for t in get_tweets(handle, pages=numPages)])
    text_model = markovify.Text(tweets)

    return text_model.make_short_sentence(280)
    """
	
#def handle(request, question_id):
	#return HttpResponse("Twitter handle is %s." % question_id)
	
#def detail(request, question_id):
	#return HttpResponse("u look at question %s." % question_id)
	
#def results(request, question_id):
	#response = "Your looking at results of question %s."
	#return HttpResponse(response % question_id)
	
#def vote(request, question_id):
	#return HttpResponse("your voting on question %s." % question_id)