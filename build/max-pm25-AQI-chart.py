import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'globalAirPollutionDataset.csv'
data = pd.read_csv(file_path)

# Group by 'CO AQI Category' and get the maximum 'CO AQI Value' for each category
max_co_aqi = data.groupby('PM2.5 AQI Category')['PM2.5 AQI Value'].max()

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(max_co_aqi.index, max_co_aqi.values)

# Add labels to each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom')  # va: vertical alignment

plt.xlabel('PM2.5 AQI Category')
plt.ylabel('Max PM2.5 AQI Value')
plt.title('Maximum PM2.5 AQI Value by PM2.5 AQI Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
