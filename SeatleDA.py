import pandas as pd

# Load the CSV file
file_path = '/Users/alexdeane/Quest1/city-of-seattle-2012-expenditures-dollars.csv'
data = pd.read_csv(file_path)

# Sum the 2012 Actual expenditures by each department
department_sums = data.groupby('Department')['2012 Actual'].sum().dropna()

# Format the sums as currency
department_sums_formatted = department_sums.apply(lambda x: "${:,.2f}".format(x))

# Print the results neatly
for department, total in department_sums_formatted.items():
    print(f"{department}: {total}")

# Save the result to a CSV file for submission
department_sums_formatted.to_csv('department_expenditures_2012.csv', header=["Total Expenditure"])
