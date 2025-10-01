import pandas as pd

def load_employee_data(path="data/employee_data.csv"):
    return pd.read_csv(path)
