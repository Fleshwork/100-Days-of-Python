#100 DAYS OF PYTHON CHALLENGE (DR.ANGELA YI COURSE) : DAY 002 Tip Calculator - Blind Attempt

zeroStore = str("0.")
oneStore = int(1)

#Get Input from User
priceTotal = input("What was the total price of your bill? ")
tipPercent = input("Tip Percent? ")
tipPercent = zeroStore + tipPercent
print(tipPercent)
numberOfDiners = input("How many people are paying? ")

#Convert strings from user input into floats
priceTotal = float(priceTotal)
tipPercent = float(tipPercent)
numberOfDiners = float(numberOfDiners)

#Print debugging


print("\n")


#Calculation of result
result = priceTotal * tipPercent

result = result / numberOfDiners

priceTotal_new = result * numberOfDiners + priceTotal
equalCost = priceTotal_new / numberOfDiners


#Convert result back to string
result = str(result)
tipPercent = str(tipPercent)
priceTotal_new = str(priceTotal_new)
equalCost = str(equalCost)

#Print the result to the user

print("The percentage you set is " +"%" + tipPercent + " giving you a total cost of " + "$" + priceTotal_new + ", which means each customer should pay " + "$" + result +
      " each toward the tip. Splitting the total equally will cost each person " + "$" + equalCost )