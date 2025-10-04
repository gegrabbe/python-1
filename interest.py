#!/usr/bin/python
# Calculate interest earned
# Saves previous inputs in datafile .wxyz.data
#
import os


class MyProperties:
    dataFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".wxyz.data")

    def __init__(self, p=0, r=0.0, n=0, y=0):
        self.principal = p
        self.rate = r
        self.n_per_year = n
        self.years = y

    def __str__(self):
        return f"Principal: {self.principal}, Rate: {self.rate}, NumberPerYear: {self.n_per_year}, Years: {self.years}"

    def read_or_default(self):
        if os.path.exists(self.dataFile):
            with open(self.dataFile) as file:
                p = int(file.readline().rstrip().split(':')[1])
                r = float(file.readline().rstrip().split(':')[1])
                n = int(file.readline().rstrip().split(':')[1])
                y = int(file.readline().rstrip().split(':')[1])
                return MyProperties(p, r, n, y)
        else:
            return MyProperties(100000, 0.0425, 12, 1)

    def store(self):
        with open(self.dataFile, "w") as file:
            file.write(f"principal:{self.principal}\n")
            file.write(f"rate:{self.rate}\n")
            file.write(f"n_per_year:{self.n_per_year}\n")
            file.write(f"years:{self.years}\n")
        return self

    def calculate_amount(self):
        return (self.principal *
                (1 + (self.rate / self.n_per_year)) ** (self.n_per_year * self.years))


print(f"MyProperties data file: {MyProperties().dataFile}")
my_props = MyProperties().read_or_default()
print(f"MyProperties: {my_props}")

principal = my_props.principal
rate = my_props.rate
numberPerYear = my_props.n_per_year
years = my_props.years

text = input(f"Principal Amount ({principal}): ")
if len(text) > 0:
    principal = int(text)
text = input(f"Interest Rate ({rate * 100.0:,.2f}%): ")
if len(text) > 0:
    rate = float(text) / 100
text = input(f"Number Per Year ({numberPerYear}): ")
if len(text) > 0:
    numberPerYear = int(text)
text = input(f"Number Of Years ({years}): ")
if len(text) > 0:
    years = int(text)

new_props = MyProperties(principal, rate, numberPerYear, years).store()
amount = new_props.calculate_amount()
interest = amount - principal
print("------------------------------------")
print(f"Principal = {principal:,.2f}")
print(f"Rate = {rate * 100.0:,.2f}%")
print(f"After {years} years")
print(f"Amount = {amount:,.2f}")
print(f"Interest earned = {interest:,.2f}")
