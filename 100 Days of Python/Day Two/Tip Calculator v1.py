

priceTotal = float(input("What was the total price of your bill? "))
tipPercent = int(input("How much tip? 10, 12 or 15%? "))
numberOfDiners = int(input("How many people are paying? "))

#pre calc

maxTotal = tipPercent /100 * priceTotal + priceTotal

#calculation

pricePerPerson = maxTotal / numberOfDiners
result = "{:.2f}".format(pricePerPerson)

#print
message = f"Each person should pay ${result}"
print(message)