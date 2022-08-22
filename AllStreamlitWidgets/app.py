# This app will contain every single streamlit widget (or as much as possible)
#
# This is mainly done following the Fanilo Andrianasolo video titled:
# "The Streamlit Epic Tutorial (part 1/2)" (Feb 28 2022)
# and subsequently part 2; https://www.youtube.com/watch?v=vIQQR_yq-8I&list=LL&index=20&t=2s&ab_channel=FaniloAndrianasolo
#
# Some may be taken from the docs, found at: https://docs.streamlit.io/library/cheatsheet
# Otherwise, comments will be made when needed
#
# LIBRARIES: streamlit, pandas

import streamlit as st
from pandas import util
import json

# --- Setup
st.title('All Streamlit widgets')

st.header('Purpose:')
st.write('This app is meant to allow the user to familiarise themselves with every streamlit widget, by putting them on display! Explanations are brief here, see the docs for more.')

st.header('How it works:')
st.write('Each widget is presented, with the corresponding code above them.')

st.header('Useful links:')
st.write('The docs can be found at: https://docs.streamlit.io/')
st.write('Emojis can be found at: https://www.webfx.com/tools/emoji-cheat-sheet/')

# --- The widgets
# - Write Widgets
st.markdown('# - Write Widgets:')

st.markdown('### :clipboard: `st.write()`')
st.write('Hello! This is a write widget. You can call almost anything here.'
         'You can also call multiple variables in one command, it\'s kinda like a print statement!')

# - Text Widgets
st.markdown('# - Text Widgets:')

st.markdown('### :clipboard: `st.title()`')
st.title('This is the title')

st.markdown('### :clipboard: `st.header()`')
st.header('This is the header')

st.markdown('### :clipboard: `st.subheader()`')
st.subheader('This is the subheader')

st.markdown('### :clipboard: `st.markdown()`')
st.markdown('''
            This is markdown, we can use markdown code in here!

            ## For example, heres a subheading

            > We can indent like this
            `Woah! its code!`
            - We 
            - Also
            - Have
            - Emojis!
            - :smile:
            ''')

st.markdown('### :clipboard: `st.caption()`')
st.caption('A caption / footnote for pictures')

st.markdown('### :clipboard: `st.code()`')
st.code('import streamlit as st')

st.markdown('### :clipboard: `st.text()`')
st.text('write some text')

st.markdown('### :clipboard: `st.latex()`')
st.latex(r'''
         \begin{equation}
            \large{ Z = \sum_{n=0}^{\infty} g_n e^{-\beta (\varepsilon_n + \varepsilon_i)} }
         \end{equation}
         ''')

# - Data Widgets
st.markdown('# - Data Widgets:')

st.markdown('### :clipboard: `st.table()`')
table = [[1, 2, 3], [4, 5, 6]]  # testing table
st.table(table)

st.markdown('### :clipboard: `st.dataframe()`')
df = util.testing.makeDataFrame()  # testing dataframe
st.dataframe(df)

st.markdown('### :clipboard: `st.metric()`')
st.metric(
         label='Temperature',
         value='32 C',
         delta='0.3 C'
         )

st.markdown('### :clipboard: `st.json()`')
with open('test_json.json', 'rb') as file:
    test_json = json.load(file)
st.json(test_json)

# - Chart Widgets
st.markdown('# - Chart Widgets:')

# Make into different files?
# Switch between 'Data Widgets' and 'Chart Widgets' etc. using sidebar
