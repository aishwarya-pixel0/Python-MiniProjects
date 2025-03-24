print("Welcome to tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10,12 or 15 "))
person = int(input("How mnay people to split the bill?"))
tip_as_percentage = tip/100
total_tip_amt = bill * tip_as_percentage
total_bill = bill + total_tip_amt
bill_per_person = round(total_bill/person,2)
print(f"Each person should pay ${bill_per_person}")