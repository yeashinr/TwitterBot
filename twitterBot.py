import tweepy

CONSUMER_KEY = '1KRABWcON69kMFoybf7LNnHcy'
CONSUMER_SECRET = 'Suga2VAxHz1eXC4dUaxhKW4E1pSJ8R4tYc1TVRtDguoZhEXKKR'
ASSCESS_KEY = '4755646102-bIA21hURxMdHKnXKrVYqqPP0RZwqhKxSgK8CtMq'
ASSCESS_SECRET = 'DCxFk5cR0wpmVesSoErWqHOjvLBVJfOxlJjJvntAgPrdK'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ASSCESS_KEY,ASSCESS_SECRET)

api = tweepy.API(auth)
tweets = api.mentions_timeline()

for tweet in tweets:

    if '#helloworld' in tweet.text.lower():
        api.update_status('@' + tweet.user.screen_name + '#Hello World Back To you',tweet.id)
        