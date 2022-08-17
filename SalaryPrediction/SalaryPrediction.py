# Following the tutorial by the "Python Engineer" YT channel
# Title: "Build A Machine Learning Web App From Scratch" (May 1 2021)
# https://www.youtube.com/watch?v=xl0N7tHiwlw&t=420s&ab_channel=PythonEngineer
# NOTE: In the tutorial a Jupyter Notebook is used, which could be useful
#
# This project will train a model on the Stack Overflow Software Developer Survey 2022 using scikit-learn
# A survey of almost 74k developers, we will use pandas to help with the pre-processing, using survey_results_public.csv file
# https://insights.stackoverflow.com/survey/
# The web-app will be created using streamlit
#
# LIBRARIES: streamlit, scikit-learn, matplotlib, pandas, numpy
#
# This scripts purpose is to create the dataframe used, perform some pre-processing, create and save the model
# there are some visuals using streamlit
# run in the usual streamlit fashion

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import pickle

def main():
    # --- Dataframe and pre-processing
    df = pd.read_csv('survey_results_public.csv')
    st.dataframe(df)  # initial dataframe

    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]  # get only the columns we want
    df = df.rename({'ConvertedCompYearly': 'Salary'}, axis=1)  # renames column to Salary
    df = df[df['Salary'].notnull()]  # only keep rows where a Salary is given
    df = df.dropna()  # gets rid of all rows with N/A listed
    df = df[df['Employment'] == 'Employed, full-time']  # only want rows where they were employed full time
    df = df.drop('Employment', axis=1)  # we can remove this column since they should all now be the same

    # Helper function to help move the rows where few people answered from that country to 'Other' (move countries with low-data)
    def shorten_categories(categories, cutoff):
        ''' Passes through categories and changes indices with value below cutoff to 'Other'
        categories must be a pandas dataframe of 2 columns, cutoff must be an integer
        '''

        # a dict that will contain all the countries we passed as key
        # if the value of that key (for this dict) is the country itself, nothing changes
        # if it is other, the map will make the dataframe change the index (when we map it afterwards)
        # dict will look like {'USA': 'USA', 'UK': 'UK', 'Namibia': 'Other', etc.}
        categorical_map = {}

        for i in range(len(categories)):  # pass through all rows
            if categories.values[i] >= cutoff:  # if the value for that index is greater than cutoff
                categorical_map[categories.index[i]] = categories.index[i]  # listed index should be passed in
            else:
                categorical_map[categories.index[i]] = 'Other'  # otherwise list as other

        return categorical_map

    country_map = shorten_categories(df.Country.value_counts(), 400)  # atleast 400 people must have answered or else that country is moved to other
    df['Country'] = df['Country'].map(country_map)  # now only countries past cutoff are the same, below and they are concatenated to Other
    df = df[df['Country'] != 'Other']  # drop the Other category

    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]  # salary must be less than 250k and more than 10k, removing outliers

    # Helper function to change 'Less than 1 year' to 0.5, and 'More than 50 years' to 50
    def clean_experience(x):
        ''' Returns a float value depending on string input
        x must be a string
        '''

        if x == 'More than 50 years':
            return 50
        elif x == 'Less than 1 year':
            return 0.5
        else:  # if it is a number, cast it to float
            return float(x)

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)  # applies function to each value

    # Helper function to format the educations listed
    def clean_education(x):
        if 'Bachelor’s degree (B.A., B.S., B.Eng., etc.)' in x:
            return 'Bachelors'
        elif 'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)' in x:
            return 'Masters'
        elif 'Other doctoral degree (Ph.D., Ed.D., etc.)' in x:
            return 'Post Grad'
        else:
            return 'Less than a Bachelors'

    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    # Our ML model cant understand the strings in Education
    # Lets use an sklearn class 'LabelEncoder' to assign a value to each that the model can understand
    le_education = LabelEncoder()
    df['EdLevel'] = le_education.fit_transform(df['EdLevel'])  # now would have '0, 1, 2, 3' rather than (example order) 'Bachelors, Masters, Post Grad, Less...'

    # Same for countries
    le_country = LabelEncoder()
    df['Country'] = le_country.fit_transform(df['Country'])

    # we now have a dataframe of Country, Education, Experience, Salary all as floating point values without major outliers

    # TODO - graphs of data throughout preprocessing
    # final dataframe after preprocessing
    st.dataframe(df)

    # --- Training the Model
    # we want the data as Salary on y-axis (the one we want to find), and others on x-axis (our parameters)
    # we should be doing train on 80% of data, test on other 20%
    # for simplicity, we are training on all data (incorrect way)
    X = df.drop('Salary', axis=1)
    y = df['Salary']

    # - Linear Regression
    # use linear regression model to fit the data
    linear_reg = LinearRegression()
    linear_reg.fit(X, y.values)

    # prediction of what the salaries should be at each X, get error compared to other values
    y_pred = linear_reg.predict(X)
    error = np.sqrt(mean_squared_error(y, y_pred))
    st.write(f'Linear Regression Error: ${error:,.02f}')  # error is pretty high, try other model

    # - Decision Tree Regressor
    dec_tree_reg = DecisionTreeRegressor(random_state=0)
    dec_tree_reg.fit(X, y.values)

    # prediction and error
    y_pred = dec_tree_reg.predict(X)
    error = np.sqrt(mean_squared_error(y, y_pred))
    st.write(f'Decision Tree Regressor Error: ${error:,.02f}')  # error stil pretty high, try another model

    # use GridSearchCV to find best parameters for DecisionTreeRegressor
    # find best max_depth parameter from our list
    max_depth = [None, 2, 4, 6, 8, 10, 12]
    parameters = {'max_depth': max_depth}

    regressor = DecisionTreeRegressor(random_state=0)
    gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')  # scoring is how we determine how good it is, based off of negated mean squared error
    gs.fit(X, y.values)
    regressor = gs.best_estimator_  # now regressor has best parameters from our list

    regressor.fit(X, y.values)

    # prediction and error
    y_pred = regressor.predict(X)
    error = np.sqrt(mean_squared_error(y, y_pred))
    st.write(f'Modified Decision Tree Regressor Error: ${error:,.02f}')  # error stil pretty high, try another model

    # --- Passing in new data to predict
    # create a numpy array with country, education, and years experience
    new_x = np.array([['United States of America', 'Masters', 15]])

    # label encoders
    new_x[:, 0] = le_country.transform(new_x[:, 0])
    new_x[:, 1] = le_education.transform(new_x[:, 1])
    new_x = new_x.astype(float)  # make all type float

    # prediction
    new_y_pred = regressor.predict(new_x)
    st.write(f'Prediction for passed in: ${float(new_y_pred):,.02f}')

    # --- Save model
    # use pickle to save to .pkl file
    data = {'model': regressor, 'le_country': le_country, 'le_education': le_education}
    with open('saved_steps.pkl', 'wb') as file:
        pickle.dump(data, file)

    # --- Opening model
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)

    regressor_loaded = data['model']
    le_country_loaded = data['le_country']
    le_education_loaded = data['le_education']

    # prediction test
    new_x = np.array([['United States of America', 'Masters', 15]])

    new_x[:, 0] = le_country_loaded.transform(new_x[:, 0])
    new_x[:, 1] = le_education_loaded.transform(new_x[:, 1])
    new_x = new_x.astype(float)  # make all type float

    new_y_pred = regressor_loaded.predict(new_x)
    st.write(f'Prediction for passed in (loaded): ${float(new_y_pred):,.02f}')

if __name__ == '__main__':
    main()
