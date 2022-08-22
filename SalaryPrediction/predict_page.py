import streamlit as st
import pickle
import numpy as np


# load model from pkl file, assign accordingly
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)

    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']


# the web page that will be shown for this section
def show_predict_page():
    # --- Title stuffs
    st.title('Software Developer Salary Prediction')

    st.write('''
             ### We need some information to predict the salary.
             ''')

    # --- Main Content
    # assign the necessary groups to select
    countries = (
                'United States of America',
                'Germany',
                'United Kingdom of Great Britain and Northern Ireland',
                'India',
                'Canada',
                'France',
                'Brazil',
                'Spain',
                'Netherlands',
                'Australia',
                'Italy',
                'Poland',
                'Sweden',
                'Russian Federation',
                'Switzerland'
                )

    educations = (
                'Less than a Bachelors',
                'Bachelors',
                'Masters',
                'Post Grad'
                )

    country = st.selectbox('Country', countries)  # variable is assigned to the value selected from tuple or list
    education = st.selectbox('Education', educations)

    experience = st.slider('Years of Experience', 0, 50, 3)  # variable assigned to value of slider; title, start, end, default

    calculate_button = st.button('Calculate Salary')  # if user wants to get prediction, returns True if clicked
    if calculate_button:
        # same prediction process as before
        x = np.array([[country, education, experience]])

        x[:, 0] = le_country.transform(x[:, 0])
        x[:, 1] = le_education.transform(x[:, 1])
        x = x.astype(float)

        y_pred = regressor.predict(x)
        st.write(f'Predicted Salary: ${float(y_pred):,.02f}')