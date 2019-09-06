from twitter_scraper import get_tweets
import markovify

user = input("Enter a twitter user: ")

for tweet in get_tweets(user, pages=25):
    print(tweet['text'])