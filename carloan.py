#!/usr/bin/python
#
# Calculate monthly payment for car loan
#

def calculate_monthly_payment(principal, annual_interest_rate, loan_term_years):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Convert loan term to number of monthly payments
    num_payments = loan_term_years * 12
    
    # Calculate monthly payment using the formula
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**num_payments) / ((1 + monthly_interest_rate)**num_payments - 1)
    
    return monthly_payment

# main #

principal_amount = 25000
text = input(f"Loan Amount ({principal_amount}): ")
if len(text) > 0:
    principal_amount = int(text)

annual_interest_rate = 5.24
text = input(f"Interest Rate ({annual_interest_rate}): ")
if len(text) > 0:
    annual_interest_rate = float(text)

loan_term_years = 5
text = input(f"Loan Term Years ({loan_term_years}): ")
if len(text) > 0:
    loan_term_years = int(text)

monthly_payment = calculate_monthly_payment(principal_amount, annual_interest_rate, loan_term_years)

print("===========================================")
print(f"Loan Amount: ${principal_amount:,}")
print(f"Interest Rate: {annual_interest_rate:,.2f}%")
print(f"Loan Term: {loan_term_years:,} years")
print(f"Monthly Payment: ${monthly_payment:.2f}")

