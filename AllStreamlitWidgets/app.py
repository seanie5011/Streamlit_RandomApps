# This app will contain every single streamlit widget (or as much as possible)
#
# This is mainly done following the Fanilo Andrianasolo video titled:
# "The Streamlit Epic Tutorial (part 1/2)" (Feb 28 2022)
# and subsequently part 2; https://www.youtube.com/watch?v=vIQQR_yq-8I&list=LL&index=20&t=2s&ab_channel=FaniloAndrianasolo
#
# Some may be taken from the docs, found at: https://docs.streamlit.io/library/cheatsheet
# Otherwise, comments will be made when needed
#
# LIBRARIES: streamlit, pandas, numpy, altair, plotly-expressm matplotlib

import streamlit as st
from pandas import util
import json
import altair as alt
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import time

# --- Setup
st.set_page_config(
    page_title='All Streamlit widgets',
    page_icon='tada',
    initial_sidebar_state='collapsed'
)

st.title('All Streamlit widgets')

st.header('Purpose:')
st.write('This app is meant to allow the user to familiarise themselves with every streamlit widget, by putting them on display! Explanations are brief here, see the docs for more.')

st.header('How it works:')
st.write('Each widget is presented, with the corresponding code above them.')

st.header('Useful links:')
st.write('The docs can be found at: https://docs.streamlit.io/')
st.write('Emojis can be found at: https://www.webfx.com/tools/emoji-cheat-sheet/')
st.write('Altair example gallery: https://altair-viz.github.io/gallery/index.html')
st.write('Streamlit components gallery: https://streamlit.io/components')

# --- The widgets
# - Write Widgets
st.markdown('# - Write Widgets:')

st.markdown('### :clipboard: `st.write()`')
st.write(
    'Hello! This is a write widget. You can call almost anything here.'
    'You can also call multiple variables in one command, it\'s kinda like a print statement!'
)

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
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Length', 'Width', 'Size']
)  # testing dataframe
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

st.markdown('### :clipboard: `st.altair_chart()`')
c = alt.Chart(df).mark_circle().encode(
    x='Length',
    y='Width',
    size='Size',
    color='Size',
    tooltip=['Length', 'Width', 'Size']
).interactive()  # altair scatter plot of random data
st.altair_chart(c)

st.markdown('### :clipboard: `st.line_chart()`')
st.line_chart(df)

st.markdown('### :clipboard: `st.bar_chart()`')
st.bar_chart(df)

st.markdown('### :clipboard: `st.area_chart()`')
st.area_chart(df)

st.markdown('### :clipboard: `st.plotly_chart()`')
f = px.scatter(
    df,
    x='Length',
    y='Width',
    color='Size'
)
st.plotly_chart(f)

st.markdown('### :clipboard: `st.pyplot()`')
fig, ax = plt.subplots()
ax.scatter(
    df['Length'],
    df['Width'],
    df['Size']
)
st.pyplot(fig)

st.markdown('### :clipboard: `st.<element>.add_rows()`')
addrows_chart = st.line_chart(df)
time.sleep(1)
addrows_chart.add_rows(df)  # adds the dataframe again after 5 second wait

# - Media Widgets
st.markdown('# - Media Widgets:')

st.markdown('### :clipboard: `st.image()`')
st.image('https://miro.medium.com/max/1400/0*7mUI9yTv9TUXCco3')

st.markdown('### :clipboard: `st.audio()`')
st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg', format='audio/ogg')

st.markdown('### :clipboard: `st.video()`')
st.video('https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed')

# - Input Widgets
st.markdown('# - Input Widgets:')

st.markdown('### :clipboard: `st.button()`')
st.button(
    'Hello World!',
    help='Click for Hello World!',
    key='button'
)  # streamlit cannot identify multiple objects of same key, so must specify different keys for objects with same text

st.markdown('### :clipboard: `st.checkbox()`')
st.checkbox(
    'Hello World!',
    help='Click for Hello World!',
    key='checkbox'
)

st.markdown('### :clipboard: `st.radio()`')
st.radio(
    'Hello World!',
    ['Radio', 'More Radio', 'Even MORE Radio'],
    help='Click for Hello World!',
    key='radio'
)

st.markdown('### :clipboard: `st.selectbox()`')
st.selectbox(
    'Hello World!',
    ['Selectbox', 'More Selectbox', 'Even MORE Selectbox'],
    help='Click for Hello World!',
    key='selectbox'
)

st.markdown('### :clipboard: `st.button()`')
st.multiselect(
    'Hello World!',
    ['Multiselect', 'More Multiselect', 'Even MORE Multiselect'],
    help='Click for Hello World!',
    key='multiselect'
)

st.markdown('### :clipboard: `st.slider()`')
st.slider(
    'Hello World!',
    value=10,
    help='Click for Hello World!',
    key='slider'
)

st.markdown('### :clipboard: `st.select_slider()`')
st.select_slider(
    'Hello World!',
    [i for i in range(5)],
    help='Click for Hello World!',
    key='select_slider'
)

st.markdown('### :clipboard: `st.text_input()`')
st.text_input(
    'Hello World!',
    help='Click for Hello World!',
    key='text_input'
)

st.markdown('### :clipboard: `st.text_area()`')
st.text_area(
    'Hello World!',
    help='Click for Hello World!',
    key='text_area'
)

st.markdown('### :clipboard: `st.number_input()`')
st.number_input(
    'Hello World!',
    help='Click for Hello World!',
    key='number_input'
)

st.markdown('### :clipboard: `st.date_input()`')
st.date_input(
    'Hello World!',
    help='Click for Hello World!',
    key='date_input'
)

st.markdown('### :clipboard: `st.time_input()`')
st.time_input(
    'Hello World!',
    help='Click for Hello World!',
    key='time_input'
)

st.markdown('### :clipboard: `st.file_uploader()`')
st.file_uploader(
    'Hello World!',
    help='Click for Hello World!',
    key='file_uploader'
)

st.markdown('### :clipboard: `st.download_button()`')
st.download_button(
    'Hello World!',
    data=df.to_csv(),
    help='Click for Hello World!',
    key='download_button'
)

st.markdown('### :clipboard: `st.camera_input()`')
st.camera_input(
    'Hello World!',
    help='Click for Hello World!',
    key='camera_input'
)  # use googles searchbar to change access

st.markdown('### :clipboard: `st.color_picker()`')
st.color_picker(
    'Hello World!',
    help='Click for Hello World!',
    key='color_picker'
)

# - Optimization
st.markdown('# - Optimization:')

st.markdown('### :clipboard: `st.session_state`')
st.write('Session States allow you to choose which variables / states are kept in between reruns / sessions, instead of being reset.')

st.markdown('### :clipboard: `@st.cache`')
st.write('This decorator on a function tells the prorgam not to change its output if the input did not change.')
st.write('There are more caching methods, which follow this:')

st.markdown('### :clipboard: `@st.experimental_memo`')
st.write('Stores outputs if input does not change, used for files like dataframes. You can set the maximum entries to store and how long to store them for, can also be cleared.')

st.markdown('### :clipboard: `@st.experimental_singleton`')
st.write('Stores outputs across users running the app. You can set the maximum entries to store and how long to store them for, can also be cleared.')

# - Layout
st.markdown('# - Layout:')

st.markdown('### :clipboard: `st.sidebar.<element>` or `with st.sidebar:`')
st.write('See the window on the left that you can open out? That\'s the sidebar!')
st.sidebar.write('We can add many widgets to the sidebar.')

st.markdown('### :clipboard: `with st.expander:`')
with st.expander('Hello World!'):
    st.write('This is an expander, we can add more widgets to it!')

st.markdown('### :clipboard: `st.container`')
st.write('We can use the container to change certain elements based on others, for example, the line below will change when you increase the number.')
number = st.number_input('This number will display on the below markdown:')
block = st.container()
block.markdown(number)

st.markdown('### :clipboard: `st.empty`')
st.write('We can use the empty to clear certain elements when we no longer need them, for example, we can make a timer below:')
placeholder = st.empty()
with placeholder:
    for second in range(5):
        st.markdown(f'''
            :hourglass: {second + 1} seconds have passed.
            ''')
        time.sleep(1)

st.markdown('### :clipboard: `st.columns`')
st.write('We can use the columns to display widgets side-by-side:')
col1, col2, col3 = st.columns(3)
with col1:
    st.button('Its a button!')
with col2:
    st.text_input('Its a text-input!')
with col3:
    st.dataframe(df)

st.markdown('### :clipboard: `st.form`')
st.write('We can use form to create a set of widgets that will not rerun until told to do so.')
with st.form('Increase the number, submit with the button:'):
    number = st.number_input('Number Input:')
    submitted = st.form_submit_button('Submit Button')

# - Other
st.markdown('# - Other:')

st.markdown('### :clipboard: `st.set_page_config`')
st.write('This must be called at the very start of the app, here we can configure things like the page-title, the icon, and more.')

st.markdown('### :clipboard: `st.error`')
st.error('This is an error.')

st.markdown('### :clipboard: `st.warning`')
st.warning('This is a warning.')

st.markdown('### :clipboard: `st.info`')
st.info('This is info.')

st.markdown('### :clipboard: `st.success`')
st.success('This is success.')

st.markdown('### :clipboard: `st.exception`')
try:
    1 / 0
except ZeroDivisionError as e:
    st.exception(e)

st.markdown('### :clipboard: `st.spinner`')
st.write('This will run the code under it with a spinner telling the user it is working. (note that pressing this button reruns the whole script, so once all code upto there has run, then the spinner activates)')
if st.button('Test the spinner.'):
    with st.spinner('Working...'):
        time.sleep(3)

st.markdown('### :clipboard: `st.progress`')
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.markdown('### :clipboard: `st.stop`')
st.write('Stops the app entirely, can use to create a field that will not let the app continue until the user has inputted a name for example.')

st.markdown('### :clipboard: `st.experimental_rerun`')
st.write('Reruns the app. Can be used to update graphs with new data over time for example.')

st.markdown('### :clipboard: `st.echo`')
with st.echo('below'):
    st.write('This runs the code but also displays it.')

st.markdown('### :clipboard: `st.help`')
st.help(st.help)

# Make into different files?
# Switch between 'Data Widgets' and 'Chart Widgets' etc. using sidebar
