# dataset 
# 
import pandas as pd
import numpy as np
reviews_df = pd.read_csv("reviews.csv") 
reviews_df = reviews_df[["listing_id","comments"]]

# filtering out invalid/empty data
reviews_df = reviews_df[reviews_df.comments != ' ']
reviews_df = reviews_df[reviews_df.comments != '  ']
reviews_df = reviews_df[reviews_df.comments != '   ']
# new line comments
reviews_df = reviews_df.replace('\n','', regex=True)
reviews_df["comments"].replace('', np.nan, inplace=True)
# drop na
reviews_df = reviews_df.dropna()
reviews_df = reviews_df.reset_index(drop=True)

# implement sentiment analysis on reviews
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# strings to numerical values
for index, row in reviews_df.iterrows():
    print("processing : ", index)
    print("processing comment : ", row["comments"])
    compound_total = 0
    compound_avg = 0
    sentences = []
    
    paragraph = row["comments"]
    lines_list = tokenize.sent_tokenize(paragraph) # each sentence in one paragraph
    sentences.extend(lines_list)
    
    for sentence in sentences:
        ss = sid.polarity_scores(sentence)
        compound_total+=ss["compound"]

    compound_avg=compound_total/len(sentences)
    reviews_df.loc[index,"overall_sentiment"] = compound_avg
    """
    positive sentiment : (compound score >= 0.05)
    neutral sentiment : (compound score > -0.05) and (compound score < 0.05)
    negative sentiment : (compound score <= -0.05) """
    
# calculating the average of the review sentiment for each listing ID 
listing_score = reviews_df.groupby(['listing_id'],as_index=False)["overall_sentiment"].mean().sort_values(by=["listing_id"])

# create a new csv file with the processed data results
listing_score.to_csv("review_score.csv", sep = ",")
