import tweepy

consumer_key = 'SaF7id87RCPFWQnWrCXfFKEgu'
consumer_secret = 'CvNdmCM9FInwbX5TIo80E0f2FhU0geRxAxiLGH4B5aFdpjZmWg'
access_token = '68732555-Vo24ky13lMmFwlLfL6F8z5dLLqSs6ba8EjRojWoU3'
access_token_secret = 'zFK8WtJlkUoc6C8LiZScAbAXfHgkxiZaGKWjH0zCrti3l'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

print('Logged in as {}'.format(twitter_api.me().name))
