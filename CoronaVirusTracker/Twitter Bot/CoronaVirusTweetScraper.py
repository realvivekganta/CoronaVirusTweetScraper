from twitter_scraper import get_tweets
import json
import datetime
import pandas as pd

# selected tag = ['#coronavirus,#Coronaoutbreak,#COVID-19, Wuhan Coronavirus,]

res_list = []
result_df = pd.DataFrame()
num_pages = 10

for i in range(1, num_pages+1):
    for tweet in get_tweets('#CoronaVirus', '#Coronaoutbreak', '#COVID-19', '#Wuhan Coronavirus', pages=i):
        tweet['time'] = str(tweet['time'])  # convert datetime object to str
        res_list.append(tweet)
