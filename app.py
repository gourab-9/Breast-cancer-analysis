import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('heart.csv')

# Define the title of the Streamlit app
st.title('Heart Disease Data Analysis')

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select an analysis to display:",
                           ['Dataset Overview',
                            'Frequency Distribution of Target Variable',
                            'Target vs Exang',
                            'Chest Pain Type Distribution',
                            'Chest Pain Type vs Target',
                            'Distribution of Maximum Heart Rate',
                            'Boxplot of Maximum Heart Rate by Target',
                            'Boxplot of Age by Target',
                            'Boxplot of Age',
                            'Boxplot of Resting Blood Pressure',
                            'Boxplot of Cholesterol',
                            'Boxplot of Maximum Heart Rate',
                            'Boxplot of ST Depression Induced by Exercise',
                            'Findings'])

# Display selected analysis
if options == 'Dataset Overview':
    st.subheader('Dataset')
    st.write(df.head())

elif options == 'Frequency Distribution of Target Variable':
    st.subheader('Frequency Distribution of Target Variable')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x="target", data=df, ax=ax)
    st.pyplot(fig)
    # Add interpretation
    st.markdown("""
    #### Interpretation
    - The above plot confirms the findings that -
      - There are 165 patients suffering from heart disease, and 
      - There are 138 patients who do not have any heart disease.
    """)


elif options == 'Target vs Exang':
    st.subheader('Target vs Exang')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x="target", hue="exang", data=df, ax=ax)
    st.pyplot(fig)

elif options == 'Chest Pain Type Distribution':
    st.subheader('Chest Pain Type Distribution')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x="cp", data=df, ax=ax)
    st.pyplot(fig)
    st.markdown('''
    #### Interpretation
        - We can see that the values of `target` variable are plotted wrt `cp`.
        - `target` variable contains two integer values 1 and 0 : (1 = Presence of heart disease; 0 = Absence of heart disease
        ''')



elif options == 'Chest Pain Type vs Target':
    st.subheader('Chest Pain Type vs Target')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x="cp", hue="target", data=df, ax=ax)
    st.pyplot(fig)

elif options == 'Distribution of Maximum Heart Rate':
    st.subheader('Distribution of Maximum Heart Rate')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.distplot(df['thalach'], bins=10, ax=ax)
    st.pyplot(fig)
    st.markdown('We can see that the thalach variable is slightly negatively skewed.')


elif options == 'Boxplot of Maximum Heart Rate by Target':
    st.subheader('Boxplot of Maximum Heart Rate by Target')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x="target", y="thalach", data=df, ax=ax)
    st.pyplot(fig)
    st.markdown('''
    #### Interpretation
    - The above boxplot confirms our finding that people suffering from heart disease (target = 1)
     have relatively higher heart rate (thalach) as compared to people who are not suffering from 
     heart disease (target = 0).''')



elif options == 'Boxplot of Age by Target':
    st.subheader('Boxplot of Age by Target')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x="target", y="age", data=df, ax=ax)
    st.pyplot(fig)
    st.markdown('''
    #### Interpretation

    - The above boxplot tells two different things :
        - The mean age of the people who have heart disease is less than the mean age of the people who do not have heart disease.
        - The dispersion or spread of age of the people who have heart disease is greater than the dispersion or spread of age of the people who do not have heart disease.
            ''')




elif options == 'Boxplot of Age':
    st.subheader('Boxplot of Age')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=df["age"], ax=ax)
    st.pyplot(fig)
    st.markdown("## Here in this AGE column we don't have any outlier")

elif options == 'Boxplot of Resting Blood Pressure':
    st.subheader('Boxplot of Resting Blood Pressure')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=df["trestbps"], ax=ax)
    st.pyplot(fig)
    st.markdown('## Resting blood pressure contains outliers to the right side.')

elif options == 'Boxplot of Cholesterol':
    st.subheader('Boxplot of Cholesterol')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=df["chol"], ax=ax)
    st.pyplot(fig)
    st.markdown('## Serum cholestoral contains outliers to the right side.')

elif options == 'Boxplot of Maximum Heart Rate':
    st.subheader('Boxplot of Maximum Heart Rate')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=df["thalach"], ax=ax)
    st.pyplot(fig)
    st.markdown('## Maximum heart rate achieved has a single outlier to the left side.')

elif options == 'Boxplot of ST Depression Induced by Exercise':
    st.subheader('Boxplot of ST Depression Induced by Exercise')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=df["oldpeak"], ax=ax)
    st.pyplot(fig)
    st.markdown('## Depression induced by exercise relative to rest contains outliers to the right side.')


elif options == 'Findings':
    st.subheader('Findings')
    st.markdown("""
    ### Findings of Univariate Analysis

    Findings of univariate analysis are as follows:

    - Our feature variable of interest is `target`.
    - It refers to the presence of heart disease in the patient.
    - It is integer valued as it contains two integers 0 and 1 - (0 stands for absence of heart disease and 1 for presence of heart disease).
    - `1` stands for presence of heart disease. So, there are 165 patients suffering from heart disease.
    - Similarly, `0` stands for absence of heart disease. So, there are 138 patients who do not have any heart disease.
    - There are 165 patients suffering from heart disease, and 
    - There are 138 patients who do not have any heart disease.
    - Out of 96 females - 72 have heart disease and 24 do not have heart disease.
    - Similarly, out of 207 males - 93 have heart disease and 114 do not have heart disease.

    ### Findings of Bivariate Analysis

    Findings of Bivariate Analysis are as follows:

    - There is no variable which has strong positive correlation with `target` variable.
    - There is no variable which has strong negative correlation with `target` variable.
    - There is no correlation between `target` and `fbs`.
    - The `cp` and `thalach` variables are mildly positively correlated with `target` variable.
    - We can see that the `thalach` variable is slightly negatively skewed.
    - The people suffering from heart disease (target = 1) have relatively higher heart rate (thalach) as compared to people who are not suffering from heart disease (target = 0).
    - The people suffering from heart disease (target = 1) have relatively higher heart rate (thalach) as compared to people who are not suffering from heart disease (target = 0).

    #### Findings

    - The `age` variable does not contain any outlier.
    - `Resting` blood pressure contains outliers to the right side.
    - `Serum cholestoral` contains outliers to the right side.
    - `Maximum heart rate` achieved has a single outlier to the left side.
    - `Depression induced by exercise relative to rest` contains outliers to the right side.
    """)