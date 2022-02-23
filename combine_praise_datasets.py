import json
import pandas as pd
import numpy as np
from datetime import datetime

# Opening JSON file
f = open('praise_samples_810180621930070088_1.json')

# returns JSON object as
# a dictionary
data = json.load(f)
unchecked = []


f_praiseDataScrape = open('Token_Engineering_Commons_praise_2.csv')
f_praiseDataGoogle = open('GoogleDiscord Praise Bot Sheet - Sheet1.csv')

praiseDataScrape = pd.read_csv(f_praiseDataScrape)
praiseDataGoogle = pd.read_csv(f_praiseDataGoogle)
praiseDataGoogle = praiseDataGoogle.iloc[1:, :6].copy()
praiseDataGoogle.rename(
    columns={'FROM': 'From', 'DATE': 'Date', 'ROOM': 'Channel', 'TO': 'To'}, inplace=True)

praiseDataGoogle = praiseDataGoogle[praiseDataGoogle['SERVER']
                                    != 'Commons Stack']

# get rid of different usernames that refer to the same person
praiseDataScrape = praiseDataScrape.replace(
    ['griff (💜, 💜)#8888'], 'griff#3281')
praiseDataScrape = praiseDataScrape.replace(
    ['Zeptimus (⏳,⏳)#3359'], 'Zeptimus#3359')
praiseDataGoogle = praiseDataGoogle.replace(
    ['griff (💜, 💜)#8888'], 'griff#3281')
praiseDataGoogle = praiseDataGoogle.replace(
    ['Zeptimus (⏳,⏳)#3359'], 'Zeptimus#3359')

praiseDataScrape = praiseDataScrape.replace(
    ['Jolie_Ze#0295'], 'aka_roro#0295')
praiseDataGoogle = praiseDataGoogle.replace(
    ['Jolie_Ze#0295'], 'aka_roro#0295')


print(praiseDataScrape.head())
print(praiseDataGoogle.head())

praiseDataScrape["Date"] = pd.to_datetime(
    praiseDataScrape['Date'])
praiseDataGoogle["Date"] = pd.to_datetime(
    praiseDataGoogle['Date'])

scrape_filtered = praiseDataScrape.loc[(
    praiseDataScrape['Date'] >= '2021-11-01') & (praiseDataScrape['Date'] < '2022-01-31')]
google_filtered = praiseDataGoogle.loc[(
    praiseDataGoogle['Date'] >= '2021-11-01') & (praiseDataGoogle['Date'] < '2022-01-31')]


new_df = pd.merge(scrape_filtered, google_filtered, on=[
    'From', 'Date', 'To'], how='outer')

only_incomplete = new_df.loc[~new_df.index.isin(new_df.dropna().index)]
print(only_incomplete.head())
only_incomplete.to_csv("only_incomplete.csv", index=False, header=False)

print(new_df.head())
new_df.to_csv("joined_dataset.csv", index=False, header=False)

# Closing file
f_praiseDataScrape.close()
f_praiseDataGoogle.close()
