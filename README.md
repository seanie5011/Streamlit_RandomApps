# Streamlit_RandomApps
## This project contains various web-apps created using Streamlit

This project is an umbrella containing various web-apps using Streamlit. These are mostly small apps, with only few functions. They are listed as follows:

1. [ExcelDashboard](#exceldashboard)
2. [SalaryPrediction](#salaryprediction)
3. [AllStreamlitWidgets](#allstreamlitwidgets)

**[User Instructions](#user-instructions)**

### ExcelDashboard

This app displays various features of a typical Sales Report Excel Spreadsheet - by collecting data using *openpyxl* and *pandas*, such as Total Sales, Average sales per transaction, etc. It uses *plotly-express* to display plots of Total Sales by hour, and Sales by product line. There is features to filter by city, customer-type, and gender - which is updated in real-time.

The Excel Spreadsheet used is supplied, *supermarkt_sales.xlsx*.

**LIBRARIES USED: streamlit, plotly-express, pandas, openpyxl**

![github_ExcelDashboard_mainpage](https://user-images.githubusercontent.com/72211395/185999249-134ae347-b13c-49b2-85f6-022841ebc852.png)

### SalaryPrediction

This app allows the user to predict the expected salary of a Software Developer, given inputs like the Country, Education Level, and Years of Experience. The machine-learning model was created using *scikit-learn*, trained on data from the [Stack Overflow Software Developer Survey 2022](https://insights.stackoverflow.com/survey/). This is a survey collecting relevant data from over 74k participants, as such, *pandas* was used to help with data handling and pre-processing. Some data-visualisation of the Salary vs Other Parameters was created using *Matplotlib*.

This app requires the user to download the survey file from the link above, and move the *survey_results_public.csv* file into the directory of this project. The user will have to run the *SalaryPrediction.py* file using the steps below to create a *.pkl* file which contains the Prediction model. Finally, the user can run the *app.py* file as below.

**LIBRARIES USED: streamlit, scikit-learn, matplotlib, pandas, numpy**

![github_SalaryPrediction_predictpage](https://user-images.githubusercontent.com/72211395/185998483-c5d91d65-cfac-4df1-8748-a4f3851a565d.png)
![github_SalaryPrediction_explorepage](https://user-images.githubusercontent.com/72211395/185998514-414bab8c-c8f1-41b3-a418-149b94cfddf3.png)

## AllStreamlitWidgets

This app contains all streamlit widgets (within reasonable use). It does not contain explanations of all these widgets, it is simply meant to be a display of these as a way to learn what streamlit has to offer.

Helper files are supplied which are used, the user must download these.

**LIBRARIES: streamlit, pandas, numpy, altair, plotly-expressm matplotlib**

![github_AllStreamlitWidgets_cover](https://user-images.githubusercontent.com/72211395/186449950-1cf02cb9-e281-4cc4-9cf0-a8a4db157cd9.png)

## User Instructions

1. Clone this project
3. Create a virtual enviroment to be used, ideally in the same folder as this project
2. Install the necessary libraries as detailed, using *pip*  
``pip install *library*``  
*Note: ensure protobuf is of version 3.20.x or lower; using ``pip install --upgrade protobuf==3.19.0``*
3. Open the terminal in the directory of the desired script (CTRL + L, type ``cmd``), or cd into it
4. Activate the Virtual Enviroment
``*venv*\Scripts\activate``
5. Run the script using Streamlit
``streamlit run *file*.py``  
*Note: To close the app, CTRL + C on the terminal then close the browser*
