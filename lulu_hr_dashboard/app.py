import streamlit as st
from utils.data_loader import load_employee_data
from utils import visualizations as vz

st.set_page_config(page_title="Lulu Hypermarket HR Dashboard", layout="wide")

st.title("📊 Lulu Hypermarket HR Insights")

# Load data
df = load_employee_data()

# Overview metrics
st.subheader("Quick Stats")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Employees", df.shape[0])
col2.metric("Avg Salary (USD)", f"${df['Salary'].mean():,.0f}")
col3.metric("Avg Leave Taken", f"{df['LeaveDaysTaken'].mean():.1f} days")
col4.metric("Avg Performance", f"{df['PerformanceRating'].mean():.2f} / 5")

# Visualizations
st.markdown("## Demographics & Distribution")
vz.plot_country_distribution(df)

st.markdown("## Salary & Performance")
vz.plot_salary_by_country(df)
vz.plot_salary_vs_performance(df)

st.markdown("## Department Insights")
vz.plot_performance_by_department(df)

st.markdown("## Leave Patterns")
vz.plot_leave_by_level(df)
