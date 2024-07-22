import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# Ignore warnings for cleaner output
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv('globalAirPollutionDataset.csv') # You can change this with your own file or path

# Display the dataset information
print(data.info())
print("\n")

# Check for missing values in the dataset
print(data.isna().sum())
print("\n")

# Display unique values for each column
for column in data.columns:
    print(f"\n\n{column}: \n{data[column].unique()}")

'''# Visualize pair plots for numeric features (if target has limited unique values)
target_variable = 'AQI Category'

# Check if the target variable is categorical and has limited unique values
if len(data[target_variable].unique()) <= 10 and data[target_variable].dtype == 'object':
    # Select numeric columns for pair plot
    numeric_columns = data.iloc[:, 2:-1].select_dtypes(include=[np.number])

    # Concatenate the selected columns and the target variable into a new DataFrame
    pairplot_data = pd.concat([numeric_columns, data[target_variable]], axis=1)

    # Create pair plots
    sns.pairplot(pairplot_data, hue=target_variable)
    plt.show()

# Calculate and plot the correlation heatmap for numeric features
numeric_columns = data.iloc[:, 2:-1].select_dtypes(include=[np.number]).columns
numeric_data_subset = data[numeric_columns]
plt.figure(figsize=(16, 8))
sns.heatmap(numeric_data_subset.corr(), annot=True, linewidths=1)
plt.title("Correlation Heatmap")
plt.show()'''

#==============================================================================#

# Perform label encoding for categorical features
for column in data.select_dtypes(include=['object']).columns:
    data[column] = LabelEncoder().fit_transform(data[column])

# Define predictor and target variables
predictor = data.columns[2:-2]
target = data.columns[-1]

# Split the data into training and testing sets
train, test = train_test_split(data, test_size=0.3, random_state=42, stratify=data[target])

# Display predictor and target variables
print(f"\nPredictors: {predictor}")
print(f"Target: {target}")

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=0)
model.fit(train[predictor], train[target])

# Evaluate the model on train data
print("\nFor Train Data")
train_pred = model.predict(train[predictor])
print(pd.crosstab(train[target], train_pred, rownames=["Actual"], colnames=["Prediction"]))
print(f"Accuracy: {accuracy_score(train_pred, train[target])}")

# Evaluate the model on test data
print("\nFor Test Data")
test_pred = model.predict(test[predictor])
print(pd.crosstab(test[target], test_pred, rownames=["Actual"], colnames=["Prediction"]))
print(f"Accuracy: {accuracy_score(test_pred, test[target])}")

def train_model(data):
    # Use all relevant features for training
    relevant_features = ['CO AQI Value', 'CO AQI Category', 'Ozone AQI Value', 'Ozone AQI Category', 'NO2 AQI Value', 'NO2 AQI Category', 'PM2.5 AQI Value', 'PM2.5 AQI Category', 'AQI Category']
    
    # Filter the dataset to include only relevant features
    relevant_data = data[relevant_features]

    # Define predictor and target variables
    predictor = relevant_data.columns[:-1]
    target    = relevant_data.columns[-1]

    # Perform label encoding for categorical features
    label_encoder     = LabelEncoder()
    
    for column in relevant_data.select_dtypes(include=['object']).columns:
        relevant_data[column] = label_encoder.fit_transform(relevant_data[column])

    # Split the data into training and testing sets
    train, test = train_test_split(relevant_data, test_size=0.3, random_state=0, stratify=relevant_data[target])

    # Train a Random Forest Classifier
    model = RandomForestClassifier(random_state=0)
    model.fit(train[predictor], train[target])

    return model, label_encoder

def predict_aqi_category(model, label_encoder, co_aqi, co_aqi_category, ozone_aqi, ozone_aqi_category, no2_aqi, no2_aqi_category, pm25_aqi, pm25_aqi_category):
    try:
        # Convert category values to numeric using label encoding
        co_aqi_category_encoded    = label_encoder.transform([co_aqi_category])[0]
        ozone_aqi_category_encoded = label_encoder.transform([ozone_aqi_category])[0]
        no2_aqi_category_encoded   = label_encoder.transform([no2_aqi_category])[0]
        pm25_aqi_category_encoded  = label_encoder.transform([pm25_aqi_category])[0]

        # Create a DataFrame with user input
        user_input = pd.DataFrame({
            'CO AQI Value'      : [co_aqi],
            'CO AQI Category'   : [co_aqi_category_encoded],
            'Ozone AQI Value'   : [ozone_aqi],
            'Ozone AQI Category': [ozone_aqi_category_encoded],
            'NO2 AQI Value'     : [no2_aqi],
            'NO2 AQI Category'  : [no2_aqi_category_encoded],
            'PM2.5 AQI Value'   : [pm25_aqi],
            'PM2.5 AQI Category': [pm25_aqi_category_encoded]
        })

        # Make the prediction
        prediction = model.predict(user_input)

        # Inverse transform label encoding to get the original category
        predicted_category = label_encoder.inverse_transform(prediction)[0]

        return predicted_category
    except ValueError:
        return 'Invalid input for AQI categories'

def determine_category(value, ranges):
    # Determine the category based on concentration level and predefined ranges.
    for i in range(len(ranges) - 1):
        if ranges[i] <= value <= ranges[i + 1]:
            category_names = ['Good', 'Satisfactory', 'Moderately Polluted', 'Poor', 'Very Poor', 'Severe']
            return category_names[i]
    return 'Undefined Category'

def predict_aqi_category_auto(co_aqi, ozone_aqi, no2_aqi, pm25_aqi):
    try:
        # Define ranges and corresponding categories for each pollutant
        co_ranges    = [   0,    1,    2,   10,   17,   31,  200]
        ozone_ranges = [   0,   50,  100,  168,  207,  300]
        no2_ranges   = [   0,   40,   69,  100]
        pm25_ranges  = [   0,   30,   60,   90,  120,  250,  500]

        # Determine categories based on concentration levels
        co_category    = determine_category(co_aqi, co_ranges)
        ozone_category = determine_category(ozone_aqi, ozone_ranges)
        no2_category   = determine_category(no2_aqi, no2_ranges)
        pm25_category  = determine_category(pm25_aqi, pm25_ranges)

        # Return the categories
        return co_category, ozone_category, no2_category, pm25_category

    except ValueError:
        return 'Invalid input values'