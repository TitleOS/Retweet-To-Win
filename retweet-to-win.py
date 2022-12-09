import tweepy
import time
import json

with open("secrets.json") as f:
    secrets_str = f.read()

# Parse the secrets from the string using the json.loads() function
secrets = json.loads(secrets_str)

# Set the keys, tokens and secrets from the secrets dictionary
consumer_key = secrets["consumer_key"]
consumer_secret = secrets["consumer_secret"]
access_token = secrets["access_token"]
access_token_secret = secrets["access_token_secret"]


# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set the access token and access token secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing the text "Retweet to win"
query = "Retweet to win"

while True:
    # Retweet and follow any tweets that match the search query
    for tweet in api.search_tweets(query):
        try:
            api.retweet(tweet.id)
            api.create_favorite(id=tweet.id)
            #api.create_friendship(tweet.user.screen_name, tweet.user.id, follow=False)
            api.create_friendship(user_id=tweet.user.id)
            print("Retweeted, liked and followed user: ", tweet.user.id)
        except tweepy.TweepyException as error:
            print("Error: ", error)
    time.sleep(3600) #Sleep for a hour to prevent rate limiting by twitter. A longer sleep would likely be better to allow for more new tweets.
