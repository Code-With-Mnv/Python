# Prompt the user for the basic salary (BS)
basic_salary = float(input("Enter the basic salary (BS): "))

# Calculate the dearness allowance (DA) as 70% of BS
dearness_allowance = 0.70 * basic_salary

# Calculate the travel allowance (TA) as 30% of BS
travel_allowance = 0.30 * basic_salary

# Calculate the house rent allowance (HRA) as 10% of BS
house_rent_allowance = 0.10 * basic_salary

# Calculate the gross salary as the sum of BS, DA, TA, and HRA
gross_salary = basic_salary + dearness_allowance + travel_allowance + house_rent_allowance

# Display the result
print(f"The gross salary is: {gross_salary}")