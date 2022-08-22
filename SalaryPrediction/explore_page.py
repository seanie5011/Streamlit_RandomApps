import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
    ''' Passes through categories and changes indices with value below cutoff to 'Other'
    categories must be a pandas dataframe of 2 columns, cutoff must be an integer
    '''

    categorical_map = {}

    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'

    return categorical_map


def clean_experience(x):
    ''' Returns a float value depending on string input
    x must be a string
    '''

    if x == 'More than 50 years':
        return 50
    elif x == 'Less than 1 year':
        return 0.5
    else:
        return float(x)


def clean_education(x):
    if 'Bachelor’s degree (B.A., B.S., B.Eng., etc.)' in x:
        return 'Bachelors'
    elif 'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)' in x:
        return 'Masters'
    elif 'Other doctoral degree (Ph.D., Ed.D., etc.)' in x:
        return 'Post Grad'
    else:
        return 'Less than a Bachelors'

@st.cache
def load_data():
    # reload all data and preprocessing, cache the result
    df = pd.read_csv('survey_results_public.csv')

    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df = df.rename({'ConvertedCompYearly': 'Salary'}, axis=1)
    df = df[df['Salary'].notnull()]
    df = df.dropna()
    df = df[df['Employment'] == 'Employed, full-time']
    df = df.drop('Employment', axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['Country'] != 'Other']

    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    return df

df = load_data()

def show_explore_page():
    # --- Title stuffs
    st.title('Explore Salary Prediction')

    st.write('''
             ### Stack Overflow Software Developer Survey 2022
             ''')

    # --- Main Content
    # get all data for each country
    data = df['Country'].value_counts()

    # - Pie-chart: of country counts
    fig, ax = plt.subplots()

    ax.pie(data, labels=data.index, autopct='%1.1f%%', shadow=True, startangle=90)  # nice looking arguments
    ax.axis('equal')  # equal sized x and y

    st.write(''' Number of Data from different Countries
             ''')

    st.pyplot(fig)  # calls plot

    # - Bar-chart: Mean salary by country
    # format the data to plot
    # get the salary vs country data
    # then get the mean and sort accordingly
    bar_chart_data = df.groupby(['Country'])['Salary']
    bar_chart_data = bar_chart_data.mean().sort_values(ascending=True)

    st.write(''' Mean Salary by Country
             ''')

    st.bar_chart(bar_chart_data)  # built in streamlit bar chart

    # - Line-cart: Mean salary by experience
    # format the data to plot
    # get the salary vs country data
    # then get the mean and sort accordingly
    line_chart_data = df.groupby(['YearsCodePro'])['Salary']
    line_chart_data = line_chart_data.mean().sort_values(ascending=True)

    st.write(''' Mean Salary by Experience
             ''')

    st.line_chart(line_chart_data)
