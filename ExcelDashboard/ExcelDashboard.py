# This is my first Streamlit web-app
# Following the tutorial by the "Coding is Fun" YT channel
# Title: "Turn An Excel Sheet Into An Interactive Dashboard Using Python (Streamlit)" (Sep 11 2021)
# https://www.youtube.com/watch?v=Sb0A9i6d320&t=543s&ab_channel=CodingIsFun
#
# This project will read the excel file as a pandas dataframe using openpyxl
# The web-app will be created using streamlit, and graph using plotly-express
#
# Ensure protobuf is of version 3.20.x or lower 'pip install --upgrade protobuf==3.19.0'
# open command prompt at this directory by opening this folder and type in 'cmd' into address bar (CTRL + L)
# activate this venv by typing: 'VenvExcelDashboard\Scripts\activate'
# your fresh line should read: '(VenvExcelDashboard) C:\Users\seani\source\repos\Python\Streamlit\Streamlit_RandomApps\ExcelDashboard>'
# now type: 'streamlit run ExcelDashboard.py'
# to close, type into terminal CTRL + C, then close page
#
# LIBRARIES: streamlit, plotly-express, pandas

import pandas as pd
import plotly.express as px
import streamlit as st

def main():
    # --- Configuration of web-app
    # set title, icon, and layout
    st.set_page_config(
        page_title='Sales Dashboard',
        page_icon=':bar_chart:',
        layout='wide'
        )

    # create pandas dataframe of excel data
    # we wrap into function so we can cache the data
    # it will not be loaded every refresh unless the file changes
    @st.cache
    def get_data_from_excel():
        df = pd.read_excel(
            io='supermarkt_sales.xlsx',
            engine='openpyxl',
            sheet_name='Sales',
            skiprows=3,
            usecols='B:R',
            nrows=1000
            )

        # Make new column - time of day in hours ('hour')
        # we want to get the hours from 'Time' in format hours:minutes:seconds
        # by default, it is not in this format (its in 24hr digital)
        # we must create the 'hour' column to be in this format
        df['hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour  # dt is datetime

        return df

    df = get_data_from_excel()

    # --- Sidebar
    # this contains our filters
    # we want to be able to filter by city, customer type, and gender
    st.sidebar.header('Please Filter Here:')

    city = st.sidebar.multiselect(
        'Select the City:',
        options=df['City'].unique(),
        default=df['City'].unique()
        )  # multiselect widget allowing the user to select a city, default values are all cities

    customer_type = st.sidebar.multiselect(
        'Select the Customer Type:',
        options=df['Customer_type'].unique(),
        default=df['Customer_type'].unique()
        )

    gender = st.sidebar.multiselect(
        'Select the Gender:',
        options=df['Gender'].unique(),
        default=df['Gender'].unique()
        )

    # Query dataframe for specific filters, the @ signals a variable
    df_selection = df.query(
        'City == @city & Customer_type == @customer_type & Gender == @gender'
        )

    # --- Mainpage
    st.title(':bar_chart: Sales Dashboard')
    st.markdown('##')

    # Top KPI's (Key Performance Indicator - value that demonstrates how effectively a company is acheiving key objectives)
    total_sales = int(df_selection['Total'].sum())  # sums all entries in Total column

    average_rating = round(df_selection['Rating'].mean(), 1)
    star_rating = ':star:' * int(round(average_rating, 0))  # round mean rating to 0 decimal places, so round to integer; make this many stars

    average_sales_per_transaction = round(df_selection['Total'].mean(), 2)

    # Display the total sales, ratings, and average sales per transaction
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader('Total Sales:')
        st.subheader(f'US $ {total_sales:,}')  # the :, formats the number into comma format, so 1000 becomes 1,000
    with middle_column:
        st.subheader('Average Rating:')
        st.subheader(f'{average_rating} {star_rating}')
    with right_column:
        st.subheader('Average Sales per Transaction:')
        st.subheader(f'US $ {average_sales_per_transaction:,}')

    st.markdown('---')

    # --- Bar Charts
    # - Sales by Product line
    # get new pandas dataframe of the old one sorted by product line
    # we want to see the sum total per product line
    # we should then plot the sum total on one axis and the product lines on the other
    sales_by_product_line = df_selection.groupby(by=['Product line']).sum()  # group by product line, then add all figures
    sales_by_product_line = sales_by_product_line[['Total']].sort_values(by='Total')  # then get all rows in total column and sort in ascending order

    # create the horizontal bar chart with total on the x-axis and the product lines on the y
    # can set the color of the bars and the template from plotly
    fig_product_sales = px.bar(
        sales_by_product_line,
        x='Total',
        y=sales_by_product_line.index,  # the product lines are the indexes of this dataframe
        orientation='h',
        title='<b>Sales by Product Line</b>',  # can use HTML to make bold text
        color_discrete_sequence=['#0083B8'] * len(sales_by_product_line),  # each bar is colored with this hex-code, the sequence by default changes the color of each bar
        template='plotly_white'  # see 'https://plotly.com/python/templates/'
        )

    # update to get rid of background color (set to white) and the grid-lines
    fig_product_sales.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis=dict(showgrid=False)
        )

    # - Sales by Hour
    # get new pandas dataframe of the old one sorted by hour, with the totals sorted ascending
    sales_by_hour = df_selection.groupby(by=['hour']).sum()
    sales_by_hour = sales_by_hour[['Total']].sort_values(by='Total')

    # create the vertical bar chart with the hours on the x and total on the y
    fig_hourly_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,  # the hours are the indexes
        y='Total',
        title='<b>Sales by Hour</b>',
        color_discrete_sequence=['#0083B8'] * len(sales_by_hour),
        template='plotly_white'
        )

    # update to get rid of background color (set to white) and the grid-lines
    fig_hourly_sales.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis=dict(tickmode='linear'),  # makes sure each hour is labeled (12, 13, 14, etc.)
        yaxis=dict(showgrid=False)
        )

    # - Display
    # Display the two bar charts side-by-side
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
    right_column.plotly_chart(fig_product_sales, use_container_width=True)

    # Display the datasets for each side-by-side
    left_column, right_column = st.columns(2)
    left_column.dataframe(sales_by_hour)
    right_column.dataframe(sales_by_product_line)

    # Display the original dataframe
    st.dataframe(df_selection)

    # --- Styling
    # We can use CSS code to hide the hamburger icon, the header, and the footer
    hide_st_style = '''
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    '''

    st.markdown(hide_st_style, unsafe_allow_html=True)  # unsafe_allow_html makes it so the CSS code is escaped

    # NOT WORKING:
    # We also created more styling by adding the .streamlit folder
    # in here, the config.toml file sets the theme
    # we have set the primary and background and secondary background and text colors, and the font

if __name__ == '__main__':
    main()
