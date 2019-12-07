import pandas as pd
df = pd.read_csv("df_done1.csv")

# drop columns
df = df.drop(columns = ['id', 'a few hours', 'a day', 'an hour', 'a few days or more','flexible', 'moderate', 'strict_14', 'strict_30'])
# change the space between words to underscore
list(df.columns)
df.columns = ['amenities',
 'host_response_rate',
 'accommodates',
 'bathrooms',
 'bedrooms',
 'beds',
 'price',
 'security_deposit',
 'cleaning_fee',
 'guests_included',
 'extra_people',
 'availability_365',
 'number_of_reviews',
 'review_scores_rating',
 'reviews_per_month',
 'summary_len',
 'houserules_len',
 'Manhattan',
 'Brooklyn',
 'Queens',
 'Others',
 'Entire_home',
 'Private_room',
 'Shared_room']


# random-forest-feature-importance-chart-using-python
import pandas as pd
df = pd.read_csv("df_done.csv")
list(df.columns)
# independent variables and dependent variable
x = df.iloc[:, 0:23].values
y = df.iloc[:, 23:24].values
 # traing set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)


import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(x,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(df.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(20,'Score'))  #print 10 best features

# fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x_train, y_train)

import matplotlib.pyplot as plt
features=df.columns
importances = regressor.feature_importances_
indices = np.argsort(importances)


plt.figure(1)
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), features[indices])
plt.xlabel('Relative Importance')


# move price to the last column and remove more columns
df = df[[
 'bathrooms',
 'bedrooms',
 'beds',
 'security_deposit',
 'cleaning_fee',
 'guests_included',
 'extra_people',
 'number_of_reviews',
 'review_scores_rating',
 'Manhattan',
 'Brooklyn',
 'Queens',
 'Entire_home',
 'Private_room',
 'Shared_room',
 'price']]


# visu outliners by boxpot
import seaborn as sns
sns.boxplot(x=df["price"])
#detect outlines use z score
import numpy as np
from scipy import stats
z = np.abs(stats.zscore(df))
#  remove outlines
threshold = 3
np.where(z > 3)

df.shape
df_o = df[(z < 3).all(axis=1)]
df_o.shape
df = df_o


# writing data to local 
df.to_csv("Final_dataset.csv", sep = ",", index = False)