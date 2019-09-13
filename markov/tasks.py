from celery import shared_task

from markov.scraper2.markovey import *

@shared_task

# Call markovey.py, which scrapes the twitter profile and then creates the tweet
def scrape_and_bake(user):

    # Get the new tweet from the main function in markovey
    return main(user)
    