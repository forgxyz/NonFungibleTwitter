import json, tweepy

with open('creds.json') as f:
    creds = json.load(f)
    consumer_key = creds['consumer_key']
    consumer_secret = creds['consumer_secret']
    access_token = creds['access_token']
    access_token_secret = creds['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api)
