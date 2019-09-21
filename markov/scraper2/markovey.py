import markovify

from .twitter_scraper2 import get_tweets


def main(user):
    
    # delete '@' from username
    if user[0] == '@':
        user = user.lstrip('@')
    
    # max number of twitter pages to scrape
    numPages = 15
    
    # Error handling for invalid usernames
    try:
        # Fetching tweets 
        tweets = '\n'.join([t['text'] for t in get_tweets(user, pages=numPages)])
        
        # Creating a sentence
        text_model = markovify.Text(tweets)

        newTweet = text_model.make_short_sentence(240)

        # Ensuring valid urls by making sure putting spaces before twitter images
        newTweet = separate_pic_url(newTweet)
        
        return newTweet

    except ValueError:
        return 'Oops, either @' + user + ' does not exist or is private :('
 
 
# Separate the url of a twitter picture from other words
def separate_pic_url(tweet):
    if tweet is None:
        return tweet
        
    tweetArr = tweet.split(' ')
    
    # Run through the array of words
    for w_count, word in enumerate(tweetArr):
        if 'pic.twitter.com' in word:
            # Slit the url from the word and add a space
            w = word.split('pic.twitter.com')
            url = 'pic.twitter.com' + w[1]
            tweetArr[w_count] = w[0] + ' ' + url
            
    # Join the array of words back into one string
    return ' '.join(tweetArr)
