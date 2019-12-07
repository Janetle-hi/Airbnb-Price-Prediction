#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 21:06:38 2019

@author: charlotte
"""

def PrintHeaders():
	print ("Status: 200 OK")
	print ("Content-type: text/html")
	print ("")

def GetInput():
	# input through URL
	import os
	input = {}
	inpStr = os.environ['QUERY_STRING']
	if inpStr != "":
		vars = inpStr.split("&")
		for var in vars:
			nameValue = var.split("=")
			name = nameValue[0]
			value = nameValue[1]
			input[name] = value
		return input
	else:
		return None

def PageStart():
	# output webpage
    print ('<!DOCTYPE html>')
    print ('  <html>')
    print ('    <head>')
    print ('      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">')
    print ('      <!--Import materialize.css-->')
    print ('      <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>')
    print ('      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>')
    print ('    </head>')
    print ('    <body>')
    print ('      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>')
    print ('      <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>')
    print ('<div class="container">')
    print ("<H1>Airbnb Lend Price Advisor</H1>")
    print ("<form action='airbnb.py' method='get'>")
    print ("Enter your neighborhood (M for Manhattan, B for Brooklyn, Q for Queens):  <input type='text' name='neighborhood'><br>")
    print ("Enter your room type (E for Entire home, P for Private room, S for Shared room): <input type='text' name='room_type'><br>")
    print ("Enter number of bathrooms: <input type='text' name='bathrooms' ><br>")
    print ("Enter number of bedrooms: <input type='text' name='bedrooms'><br>")
    print ("Enter number of beds: <input type='text' name='beds' ><br>")
    print ("Enter amount of security deposits ($): <input type='text' name='security_deposit' ><br>")
    print ("Enter amount of cleaning fee ($): <input type='text' name='cleaning_fee' ><br>")
    print ("Enter number of guests: <input type='text' name='guests_included' ><br>")
    print ("Number of extra people: <input type='text' name='extra_people'><br>")
    print ("Number of reviews: <input type='text' name='number_of_reviews'><br>")
    print ("Enter review scores rating (0-100): <input type='text' name='review_scores_rating'><br>")

	
    print("<input type='submit' value='Submit'>")
    print("</form>")

def PageEnd():
	print ('</div>')
	print ('    </body>')
	print ('  </html>')
	
def Process():
	
    if input == None or input["neighborhood"] == None:
        return
    
    import pandas as pd

    df = pd.read_csv('cis9650/Final_dataset.csv')

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
    regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
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
    
    n = input["neighborhood"]
    n = n.upper()
    if n == "M":
        test_values.loc[0,'Manhattan'] = 1
        test_values.loc[0,'Brooklyn'] = 0
        test_values.loc[0,'Queens'] = 0
    elif n == "B":
        test_values.loc[0,'Manhattan'] = 0
        test_values.loc[0,'Brooklyn'] = 1
        test_values.loc[0,'Queens'] = 0
    elif n == "Q":
        test_values.loc[0,'Manhattan'] = 0
        test_values.loc[0,'Brooklyn'] = 0
        test_values.loc[0,'Queens'] = 1
        
    
    r = input["room_type"]
    r = r.upper()
    if r == "E":
        test_values.loc[0,'Entire_home'] = 1
        test_values.loc[0,'Private_room'] = 0
        test_values.loc[0,'Shared_room'] = 0
    elif r == "P":
        test_values.loc[0,'Entire_home'] = 0
        test_values.loc[0,'Private_room'] = 1
        test_values.loc[0,'Shared_room'] = 0
    elif r == "S":
        test_values.loc[0,'Entire_home'] = 0
        test_values.loc[0,'Private_room'] = 0
        test_values.loc[0,'Shared_room'] = 1
    

    test_values.loc[0,'Number of bathrooms:'] = float(input["bathrooms"])
    test_values.loc[0,'Number of bedrooms:'] = float(input["bedrooms"])
    test_values.loc[0,'Number of beds:'] = float(input["beds"])
    test_values.loc[0,'Amount of security deposits ($):'] = float(input["security_deposit"])
    test_values.loc[0,'Amount of cleaning fee ($):'] = float(input["cleaning_fee"])
    test_values.loc[0,'Number of guests:'] = float(input["guests_included"])
    test_values.loc[0,'Number of extra people:'] = float(input["extra_people"])
    test_values.loc[0,'Number of reviews:'] = float(input["number_of_reviews"])
    test_values.loc[0,'Review scores rating (0-100):'] = float(input["review_scores_rating"])

    new_pred = regressor.predict(test_values)

    print("<h1>We suggest price $",new_pred[0],"per night</h1>")
    print("You entered: \n", test_values.to_html())
    print("<br /><br /><br /><br /><br />")
    
    
        
	
# GET INPUT TO THE PAGE	
input = GetInput()

# RENDER THE PAGE
PrintHeaders()
PageStart()
Process()
PageEnd()