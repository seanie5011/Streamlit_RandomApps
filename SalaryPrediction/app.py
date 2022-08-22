import streamlit as st
import pickle
import numpy as np

from predict_page import show_predict_page
from explore_page import show_explore_page

# use sidebar to choose which sites to use
page = st.sidebar.selectbox('Explore or Predict', ('Predict', 'Explore'))  # a selectbox to select Predict or Explore on the sidebar

if page == 'Predict':
    show_predict_page()
elif page == 'Explore':
    show_explore_page()
