bill = float(input("What was the total bill?"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people shall pay the bill?"))

percent_tip = tip / 100

tip_amount = bill * percent_tip

total_tip = bill + tip_amount

people_bill = total_tip / people

final_amount = round(people_bill, 2)

print(f"You shall pay {final_amount}")