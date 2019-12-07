

# import dataset 
import pandas as pd
df = pd.read_csv("Final_dataset.csv")

#change column names to make it clearer 
df.rename(columns={'bathrooms':'Number of bathrooms:'},inplace=True)
df.rename(columns={'bedrooms':'Number of bedrooms:'},inplace=True)
df.rename(columns={'beds':'Number of beds:'},inplace=True)
df.rename(columns={'security_deposit':'Amount of security deposits ($):'},inplace=True)
df.rename(columns={'cleaning_fee':'Amount of cleaning fee ($):'},inplace=True)
df.rename(columns={'guests_included':'Number of guests:'},inplace=True)
df.rename(columns={'extra_people':'Number of extra people:'},inplace=True)
df.rename(columns={'number_of_reviews':'Number of reviews:'},inplace=True)
df.rename(columns={'review_scores_rating':'Review scores rating (0-100):'},inplace=True)

# independent variables and dependent variable
x = df.iloc[:, 0:15].values
y = df.iloc[:, 15].values

 # traing set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

# fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 128, random_state = 0)
regressor.fit(x_train, y_train)

# predict y value using x test set
y_pred = regressor.predict(x_test)

# find correlation between y predict and y test
from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_pred)
# more info, please refer to https://en.wikipedia.org/wiki/Entropy_(information_theory)

# asking house owners to provide details of their house and predict price for him/her
collists = list(df.columns)
collists.remove('price')
test_values = pd.DataFrame(columns = collists)

neighborhood = input("Enter your neighborhood : M for Manhattan, B for Brooklyn, Q for Queens: ")
neighborhood = neighborhood.upper()
if neighborhood == "M":
    test_values.loc[0,'Manhattan'] = 1
    test_values.loc[0,'Brooklyn'] = 0
    test_values.loc[0,'Queens'] = 0
elif neighborhood == "B":
    test_values.loc[0,'Manhattan'] = 0
    test_values.loc[0,'Brooklyn'] = 1
    test_values.loc[0,'Queens'] = 0
elif neighborhood == "Q":
    test_values.loc[0,'Manhattan'] = 0
    test_values.loc[0,'Brooklyn'] = 0
    test_values.loc[0,'Queens'] = 1
    
room_type = input("Enter your room type : E for Entire home, P for Private room, S for Shared room : ")
room_type = room_type.upper()
if room_type == "E":
    test_values.loc[0,'Entire_home'] = 1
    test_values.loc[0,'Private_room'] = 0
    test_values.loc[0,'Shared_room'] = 0
elif room_type == "P":
    test_values.loc[0,'Entire_home'] = 0
    test_values.loc[0,'Private_room'] = 1
    test_values.loc[0,'Shared_room'] = 0
elif room_type == "S":
    test_values.loc[0,'Entire_home'] = 0
    test_values.loc[0,'Private_room'] = 0
    test_values.loc[0,'Shared_room'] = 1
    
print("Please enter the following values")    
for collist in collists:
    if (collist != 'Manhattan' and collist != 'Brooklyn' and collist != 'Queens') and (collist != 'Entire_home' and collist != 'Private_room' and collist != 'Shared_room'):
        inputData = input(collist)
        test_values.loc[0,collist] = float(inputData)
    
new_pred = regressor.predict(test_values)
print("You entered: \n", test_values)
print("we suggest price $",new_pred[0],"per night")


#Testing plot
#1. Line plot
import matplotlib.pyplot as plt  
predict =regressor.predict(x_test)
df_test= pd.DataFrame({'Number':list(range(len(y_test))),'Actual':y_test,'Predict':predict})
df_test_100=df_test.head(101)
Number = df_test_100['Number']
Actual = df_test_100['Actual']
Predict = df_test_100['Predict']
plt.plot(Number, Actual, 'b-', label='Actual')
plt.plot(Number, Predict, 'g-', label='Predicted')
plt.legend(loc='upper left')
plt.title('Predicted Results vs Actual Results')
plt.ylabel('Price per night($)')

#2.Bar plot 
import matplotlib.pyplot as plt  
predict =regressor.predict(x_test)
df= pd.DataFrame({'Actual':y_test,'Predict':predict})
df1 = df.head(51)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.legend(loc='upper left')
plt.title('Predicted Results vs Actual Results')
plt.ylabel('Price per night ($)')
plt.show()





