import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 


df = pd.read_csv('data.csv')
print(df.head())

# Assuming df is your DataFrame
df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y %I:%M:%S %p")
  # Convert 'Date' to datetime object

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Date', y='Observation_Max_Wind')
plt.title('Max Wind Speed Over Time')
plt.xlabel('Date')
plt.ylabel('Max Wind Speed')
plt.show()

