print("Welcome to the tip calculator!")
# ask for the total bill
total_bill = float(input("What was the total bill? \n$"))
# ask for the % tip
tip = int(input("What percentage tip would you like to give? \n"))
percentage_tip = tip / 100
# multiply total bill by % tip, add the result to the total bill
final_bill = (total_bill * percentage_tip) + total_bill
# ask for the number of people splitting the bill
no_of_people = float(input("How many people are splitting this bill? \n"))
# divide the final bill by the number of people, round up the result to 2 decimal places
each_bill = "{:.2f}".format(final_bill / no_of_people)
print(f"Each person should pay: ${each_bill}")
