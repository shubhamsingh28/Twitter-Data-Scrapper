# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:37:48 2018

@author: Shubham
"""


import tweepy
import json
import tweepy
consumer_key = "G6KkNVwCUGoG97IMbuXbRDyup"
consumer_secret = "XKG5sxzjbEWrPgK785gm57NLFrQllD63t8In3s2pExeQArb2Am"
access_key = "931787785459048450-bnaxVOYWOHw0gbNB63NMiRtvTidJoDx"
access_secret = "1aOvYPF1FQTQZ3TyrIZelEGfDfjmvrwuMUk43SocKrtnx"
 
def get_tweets(id1):
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
        # Calling api
        api=tweepy.API(auth,retry_count=3,retry_delay=15,retry_errors=set([401, 404, 500, 503]), wait_on_rate_limit_notify=False ,wait_on_rate_limit=True,)
        stat=api.get_status(id1)
        return stat.user.id
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    #get_tweets("SalmanKhan_")
    print(get_tweets("260244087901413376"));