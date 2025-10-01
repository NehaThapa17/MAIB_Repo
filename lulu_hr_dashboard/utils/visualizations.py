import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_salary_by_country(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Country', y='Salary', ax=ax)
    ax.set_title('Salary Distribution by Country')
    st.pyplot(fig)

def plot_performance_by_department(df):
    fig, ax = plt.subplots()
    sns.barplot(data=df, x='Department', y='PerformanceRating', ci=None, ax=ax)
    ax.set_title('Average Performance Rating by Department')
    st.pyplot(fig)

def plot_leave_by_level(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Level', y='LeaveDaysTaken', ax=ax)
    ax.set_title('Leave Taken by Level')
    st.pyplot(fig)

def plot_salary_vs_performance(df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='Salary', y='PerformanceRating', hue='Level', ax=ax)
    ax.set_title('Salary vs Performance Rating by Level')
    st.pyplot(fig)

def plot_country_distribution(df):
    fig, ax = plt.subplots()
    df['Country'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    ax.set_title('Employee Distribution by Country')
    st.pyplot(fig)
