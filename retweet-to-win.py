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

# Queries to search tweets for. You can add more queries if you want.
queries = ["Retweet to win", "Giveaway", "Follow to win", "Like to win"]

while True:
    #Iterate over the queries
    for query in queries:
    # Search for tweets containing the current query text
        for tweet in api.search_tweets(query):
            try:
                print("Searching for query: ", query)
            # Retweet and follow the user who posted the tweet
                api.retweet(tweet.id)
                api.create_favorite(id=tweet.id)
                api.create_friendship(user_id=tweet.user.id)
                print("Retweeted, liked and followed user: ", tweet.user.screen_name)
            except tweepy.TweepyException as error:
                print("Error: ", error)
    time.sleep(2700) #Sleep for fourty-five minutes to allow for new tweets. Could be optimized.

