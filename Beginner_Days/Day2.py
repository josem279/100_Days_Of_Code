# Data Types and String manipulation

print("Welcome to the tip calculator!")

total_bill = int(input("What was the total bill?\n"))
tip_pct = input("What percent tip would you like to give\n?")
tip_pct = 1 + (int(tip_pct) / 100)
party_count = int(input("How many people split the bill?\n"))

print(f"Each person should pay: ${round(total_bill * tip_pct / party_count, 2)}")