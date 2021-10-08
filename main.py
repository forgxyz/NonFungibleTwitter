import json, tweepy
import pandas as pd
from datetime import datetime

def main():

    # initialize tweepy object
    with open('creds.json') as f:
        creds = json.load(f)
        auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
        auth.set_access_token(creds['access_token'], creds['access_token_secret'])
        api = tweepy.API(auth)
        del creds

    # load list
    with open('account_list.json') as f:
        list = json.load(f)

    # start an empty df
    df = pd.DataFrame()

    for acct in list:
        user = api.get_user(screen_name=acct)
        data = {'account': user.screen_name, 'followers': user.followers_count, 'timestamp': datetime.now()}
        df = df.append(data, ignore_index=True)

    return df


if __name__ == '__main__':
    print(main())
