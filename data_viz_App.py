import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st

container = st.container()
col1, col2 = st.columns(2)

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

def sort_data(df):
    st.sidebar.header("Data Sorting")

    # Data Sorting
    sort_column = st.sidebar.selectbox("Sort by", df.columns)
    df = df.sort_values(by=sort_column)
    return df

def group_by(df):

    #Grouping Data by categories
    group_column = st.sidebar.selectbox("Group by Sum", df.columns)
    grouped_df = df.groupby(group_column).sum()
    return grouped_df

def group_by_mean(df):
    
    #Grouping Data by mean values
    group_mean_column = st.sidebar.selectbox("Group by Mean", df.columns)
    grouped_mean_df = df.groupby(group_mean_column).mean()
    return grouped_mean_df


def data_analysis(data):
    # Execute data analysis tasks
    container.write("# Data Analysis #")
    container.write("First five records")
    container.write(data.head())
    container.write("Summarised Description")
    container.write(data.describe())
    container.write("Data Correlation")
    container.write(data.corr())
    container.write("Data Ranking")
    container.write(data.rank())

    sorted_df = sort_data(data)

    container.write("Data Sorting")
    container.write(sorted_df)

    groupBySum = group_by(data)

    container.write("Group By Sum")
    container.write(groupBySum)

    groupByMean = group_by_mean(data)

    container.write("Group By Mean")
    container.write(groupByMean)

    with col1:
        st.write("Columns Names: ", data.columns)
    with col1:
        st.write("Columns Data Types: ", data.dtypes)
    
    with col2:
        st.write("Missing Values: ", data.isnull().sum())

    with col2:
        st.write("Unique Values: ", data.nunique())
    
    with col2:
        st.write("Standard Deviation: ", data.std())

    with col1:
        st.write("Number of records: ", data.shape[0])
    
    with col1:
        st.write("Number of columns: ", data.shape[1])
    

def create_charts(chart_type, data, x_column, y_column):
    container.write(" # Data Visualization # ")
        
    if chart_type == "Bar":
        st.header("Bar Chart")
        fig = px.bar(data, x=x_column, y=y_column, color='Country')
        st.plotly_chart(fig)
        
    elif chart_type == "Line":
        st.header("Line Chart")
        fig = px.line(data, x=x_column, y=y_column, color='Country')
        st.plotly_chart(fig)
        
    elif chart_type == "Scatter":
        st.header("Scatter Chart")
        fig = px.scatter(data, x=x_column, y=y_column, color='Country')
        st.plotly_chart(fig)
        
    elif chart_type == "Histogram":
        st.header("Histogram")
        fig = px.histogram(data, x=x_column, y=y_column, color='Country')
        st.plotly_chart(fig)
        
    elif chart_type == "pie":
        st.header("Pie Chart")
        fig = px.pie(data, x=x_column, y=y_column, color='Country')
        st.plotly_chart(fig)


def main():
    image = Image.open("ddd.PNG")

    container.image(image, width = 200)

    container.write(" # Data Analysis and Visualization # ")
    container.write(" # Please upload csv file from sidebar # ")
    st.sidebar.image(image, width=50)
    file = st.sidebar.file_uploader("Upload a dataset in csv or Excel format", type=["csv", "excel"])

    options = st.sidebar.radio('Pages', options = ['Data Analysis', 'Data Visualization'])
    if file is not None:
        data = load_data(file)

        if options == 'Data Analysis':
            data_analysis(data)

        if options == 'Data Visualization':

            #Create a sidebar for user options
            st.sidebar.title("Chart Options")

            chart_type = st.sidebar.selectbox("Select a chart type", ["Bar", "Line", "Scatter", "Histogram", "Pie"])
            x_column = st.sidebar.selectbox("Select the X column", data.columns)
            y_column = st.sidebar.selectbox("Select the Y column", data.columns)

            create_charts(chart_type, data, x_column, y_column)

if __name__ == "__main__":
    main()

    