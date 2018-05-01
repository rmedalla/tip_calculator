total_cost = float(input("Enter total amount: "))
tip = int(input("Enter tip %: "))
tip_percentage = total_cost * .01
total_with_tip = total_cost + (tip * tip_percentage)

print(total_with_tip)
