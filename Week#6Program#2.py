#UNWSP Programming PythonCos2005DEsp25
#Week#5_Program#2_Tax Rate
#02/28/2025
#Abraham. N. Andersen

def calculate_sales_tax(total_sales):
  """
  This function calculates the county and state sales tax.

  It takes the total sales as input and returns the amounts of
  county tax, state tax, and the total tax.

  Args:
    total_sales: The total sales amount for the month.

  Returns:
    A tuple containing:
      - The county sales tax amount.
      - The state sales tax amount.
      - The total sales tax amount.
  """

  # These are the tax rates (like percentages, but as decimals)
  state_tax_rate = 0.05  # 5% state tax
  county_tax_rate = 0.025 # 2.5% county tax

  # Calculate the amounts of tax
  county_tax = total_sales * county_tax_rate
  state_tax = total_sales * state_tax_rate
  total_tax = county_tax + state_tax

  # Send back the results
  return county_tax, state_tax, total_tax

# Let's get the total sales from the user
total_sales = float(input("Enter the total for sales for this month: $"))

# Calculate the taxes using our function
county_tax, state_tax, total_tax = calculate_sales_tax(total_sales)

# Display the results
print(f"County Sales Tax: ${county_tax:.2f}")
print(f"State Sales Tax: ${state_tax:.2f}")
print(f"Total Sales Tax: ${total_tax:.2f}")