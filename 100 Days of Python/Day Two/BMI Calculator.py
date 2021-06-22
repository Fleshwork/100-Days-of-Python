#day 2 BMI Calculator

#get input from user

userHeight = input("Please enter your height in Metric : ")
userWeight = input("Please enter your weight in Metric : ")

#convert stings to floats
userWeight = float(userWeight)
userHeight = float(userHeight)

#calculate BMI
result = userWeight / userHeight ** 2


#Equation could also be writter as
#userHeight_squared = userHeight * userHeight
#result = userWeight / userHeight_squared

#convert answer back to int to remove decimals
result = int(result)

#convert answer back to string for print
result = str(result)

print("Your BMI is : " + result)