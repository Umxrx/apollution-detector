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
    
q, w, e, r = predict_aqi_category_auto(2,101,41,31)
print(q, w, e, r)