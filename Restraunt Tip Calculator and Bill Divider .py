print("Welcome to the tip calculator and bill divider!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip1=tip/100
tip_add=bill+(bill*tip1)

final=tip_add/people

print(f"Each person should pay:{round(final,2)}")
