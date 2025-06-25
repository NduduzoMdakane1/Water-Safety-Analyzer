import pandas as pd

"""
Water Safety Analyzer: Metal Concentration Checker

This code analyzes metal concentration data from an Excel file and evaluates safety levels.

What it does:
- Compares calculated concentrations of metals to reference safe limits
- Applies a customizable safety margin for each metal
- Classifies each metal as 'Safe', 'Unsafe', or 'Borderline'
- Outputs a clear summary including safety status for each entry

Could be useful for basic water quality checks using lab data (e.g. AAS or ICP-OES results).
"""


# Load Excel file
df = pd.read_excel("Water Safety Data Sheet for Metals.xlsx")

'''Create a function that compares the calculated experimental values to the reference values.
Ideally, the calculated values has to be less than the reference values for water to be safe.'''
def classify_safety(calculated_value, reference_value, margin_percent):
    lower_bound = reference_value - reference_value * (margin_percent / 100)
    upper_bound = reference_value + reference_value * (margin_percent / 100)

    if calculated_value > upper_bound:
        return 'Unsafe'
    elif calculated_value < lower_bound:
        return 'Safe'
    else:
        return 'Borderline' #This is when the calculated and the reference values are quite close.

#Create a new column named "Safety Status" where safety statuses will be displayed.
safety_statuses = []

#Loop through the rows in the Excel file and call the function "classify_safety" above to determine the status.
for index, row in df.iterrows():
    calculated = row['Concentration']     # Actual column names on the Excel File
    reference = row['SafeLimit']
    margin = row['MarginPercent']

    status = classify_safety(calculated, reference, margin)
    safety_statuses.append(status)

#Add a new column named "Safety Status" and display safety statuses there.
df['Safety Status'] = safety_statuses


#Print the new dataframe.
print(df)


# Save and export the new updated dataframe as an Excel file
df.to_excel('Analyzed Water Safety Data Sheet for Metals.xlsx', index=False)




