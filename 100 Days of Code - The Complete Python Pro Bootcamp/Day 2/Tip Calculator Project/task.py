print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# percentage: 12% -> 12/100 = 0.12
total_bill = bill + (bill * (tip/100))
total_split = total_bill/people
print(total_bill)
print(round(total_split,2))