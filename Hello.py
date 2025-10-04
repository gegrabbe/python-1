print('Hello World!')

# Calculate interest earned
#
principal = 40000
rate = 0.0425
numberPerYear = 4
years = 1
amount = principal * (1 + (rate / numberPerYear)) ** (numberPerYear * years)
interest = amount - principal
print(f"Principal = {principal:,.2f}")
print(f"Rate = {rate * 100:,.2f}%")
print(f"After {years} years")
print(f"Amount = {amount:,.2f}")
print(f"Interest earned = {interest:,.2f}")
