# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:30:02 2017

@author: Tania
Modified by Darren on 3 Mar 2018.
"""

import tweepy

consumer_key = 'SaF7id87RCPFWQnWrCXfFKEgu'
consumer_secret = 'CvNdmCM9FInwbX5TIo80E0f2FhU0geRxAxiLGH4B5aFdpjZmWg'
access_token = '68732555-Vo24ky13lMmFwlLfL6F8z5dLLqSs6ba8EjRojWoU3'
access_token_sec = 'zFK8WtJlkUoc6C8LiZScAbAXfHgkxiZaGKWjH0zCrti3l'

def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_sec)
    return tweepy.API(auth)


def collect_tweets(keyword, stop_num):
    keyword = keyword.strip()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword, limit=stop_num)
    show_content(tweets)

def stalker(victim, no):
    "This will find a certain number of tweets from our victim"
    tweets = twitter.user_timeline(screen_name=victim, count=no)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))


def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)

def post_tweet(status):
    twitter.update_status(status=status)


def see_timeline(no):
    for tweet in tweepy.Cursor(twitter.home_timeline).items(no):
        print("\n {} tweeted by {}".format(tweet.text, tweet.user.name))



if __name__ == '__main__':

    twitter = authenticate()

    # If the authentication was successful, you should
    # see the name of the account print out
    print('You are now logged in as {}'.format(twitter.me().name))
    collect_tweets('#ShefCodeFirst', 10)

    # Retrieves a single tweet from our Twitter home time line
    # and wraps it in a special, "list-like" Cursor structure from
    # the tweepy library so that we can loop through it using a for-loop.
    for status in tweepy.Cursor(twitter.home_timeline).items(1):
        # Process a single status
        print(status._json)
        # Saving the Json in a variable
        json_var = status._json

    post_tweet('Tweeting from Python in a #ShefCodeFirst class!')
