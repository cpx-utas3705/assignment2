import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("coffee-shop-sales-revenue.csv",sep='|')

data['transaction_date'] = pd.to_datetime(
data['transaction_date']
)

data_range = f"{data['transaction_date'].max() }"
print(f"Data range: {data_range.days} days")
start_date=input("Enter start date (YYYY-MM-DD): ")
end_date=input("Enter end date (YYYY-MM-DD): ")
weekly_data= pd.date_range( start_date,end_date).to_series().resample('W').sum()