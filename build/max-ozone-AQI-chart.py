import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'globalAirPollutionDataset.csv'
data = pd.read_csv(file_path)

# Group by 'CO AQI Category' and get the maximum 'CO AQI Value' for each category
max_co_aqi = data.groupby('Ozone AQI Category')['Ozone AQI Value'].max()

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(max_co_aqi.index, max_co_aqi.values)

# Add labels to each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom')  # va: vertical alignment

plt.xlabel('Ozone AQI Category')
plt.ylabel('Max Ozone AQI Value')
plt.title('Maximum Ozone AQI Value by Ozone AQI Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
