# Retweet-To-Win
A simple python bot to enter "retweet to win" style contests.

# How it works
The bot is quite simple in functionality, after an initial run, every hour, the script will search Twitter for the phrase "Retweet to win", before liking, retweeting and following the poster of the tweet, as required by many RTW style contests. I'd recommend enabling email notifications for DMs so you don't have to check the account manually for winnings. 

# How do I setup secrets.json?

Sign up for a Twitter developer account ON THE ACCOUNT YOU WANT TO USE WITH THE SCRIPT at https://developer.twitter.com. Afterwards, create an app and project, filling out the questions vaguely. Once your bot has been created, save the API key and API secret, these are the consumer key and secret. Navigate to Keys and Tokens and generate an access token and access token secret, which you should also save. Fill in the following JSON using your values, and save it as secrets.json next to the script.

```JSON
{
    "consumer_key" : "",
    "consumer_secret" : "",
    "access_token" : "",
    "access_token_secret" : ""
}
```

## Requirements
Python 3
  -tweepy
  
## Note
I am not responsible if your Twitter account is banned, your IP is blacklisted, and your house is raided by Elon Musk. By using this script, you agree that the creator is in no way responsible for its actions. 
