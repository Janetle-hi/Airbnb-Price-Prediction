#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:29:43 2019

@author: ziboxu
"""

import seaborn as sns
import pandas as pd  

df = pd.read_csv('df_done.csv')
df.shape

#Variables 
df.columns
#Explantory data analysis: No clear linear relationships 

sns.pairplot(data=df,
             x_vars=['price'],
             y_vars=['amenities', 'host_response_rate', 'accommodates',
       'bathrooms', 'bedrooms', 'beds','security_deposit','cleaning_fee', 'guests_included', 'extra_people', 'availability_365',
       'number_of_reviews', 'review_scores_rating', 'reviews_per_month',
       'summary_len', 'houserules_len','a few hours', 'a day', 'an hour',
       'a few days or more', 'Manhattan', 'Brooklyn', 'Queens', 'Others',
       'Entire home', 'Private_room','Shared_room','flexible','moderate',
       'strict_14','strict_30'])