#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you give? 10, 12, or 15? ")
person = input("How many people to split the bill? ")

# create tip calculation
billplustip = float(bill) * (1 + int(tip) / 100)
billperperson = round(billplustip / int(person), 2)
billperperson = "{:.2f}".format(billplustip / int(person))

print(f"\nTotal bill plus tip: ${billplustip}")
print(f"Each person should pay: ${billperperson}")