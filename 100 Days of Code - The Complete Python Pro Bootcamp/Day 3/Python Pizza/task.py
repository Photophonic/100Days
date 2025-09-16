print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
total = 0

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

if size == "S":
    total = 15
elif size == "M":
    total = 20
elif size == "L":
    total = 25
else:
   print("Please enter a valid size.")

if pepperoni == "Y":
    if size == "S":
        total +=2
    else:
        total +=3

if extra_cheese == "Y":
    total +=1

print(f"Your final bill is: ${total}.")