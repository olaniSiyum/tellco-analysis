import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to plot each analysis
def plot_user_overview():
    st.title("User Overview Analysis")
    
    # Get top 10 most frequent handset types
    top_handsets = df_agg['Handset Type'].value_counts().head(10).index
    # Filter the DataFrame for these handset types
    df_top_handsets = df_agg[df_agg['Handset Type'].isin(top_handsets)]
    
    # Plot the data
    fig, ax = plt.subplots()
    sns.countplot(data=df_top_handsets, x='Handset Type', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    st.pyplot(fig)  # Render the plot
    plt.close(fig)  # Close the plot to prevent overlapping in the next render

# Load the aggregated data
df_agg = pd.read_csv('../data/clean_data.csv')
if df_agg.empty:
    st.warning("The dataset is empty or not loaded properly.")
else:
    # Check the column names
    st.write("Columns in the DataFrame:")
    st.write(df_agg.columns)

    # Proceed with plots if data is available
    plot_user_overview()

def plot_user_engagement():
    st.title("User Engagement Analysis")
    # Check if 'Handset Manufacturer' exists
    if 'Handset Manufacturer' in df_agg.columns:
        # Plot related to engagement analysis
        fig, ax = plt.subplots()
        sns.boxplot(data=df_agg, y='Total DL (Bytes)', x='Handset Manufacturer', ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.error("Column 'Handset Manufacturer' not found in the dataset.")

def plot_experience_analysis():
    st.title("Experience Analysis")
    # Check if 'Avg RTT DL (ms)' exists
    if 'Avg RTT DL (ms)' in df_agg.columns and 'Handset Type' in df_agg.columns:
        # Experience related visualizations
        fig, ax = plt.subplots()
        sns.barplot(data=df_agg, y='Avg RTT DL (ms)', x='Handset Type', ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.error("Columns 'Avg RTT DL (ms)' or 'Handset Type' not found in the dataset.")

def plot_satisfaction_analysis():
    st.title("Satisfaction Analysis")
    # Satisfaction score related visualizations
    if 'Engagement Score' in df_agg.columns and 'Satisfaction Score' in df_agg.columns:
        fig, ax = plt.subplots()
        sns.scatterplot(data=df_agg, x='Engagement Score', y='Satisfaction Score', ax=ax)
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.error("Columns 'Engagement Score' or 'Satisfaction Score' not found in the dataset.")

# Main dashboard navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Select a Page", 
                         ["User Overview", "User Engagement", "Experience Analysis", "Satisfaction Analysis"])

# Display the corresponding page
if pages == "User Overview":
    plot_user_overview()
elif pages == "User Engagement":
    plot_user_engagement()
elif pages == "Experience Analysis":
    plot_experience_analysis()
elif pages == "Satisfaction Analysis":
    plot_satisfaction_analysis()