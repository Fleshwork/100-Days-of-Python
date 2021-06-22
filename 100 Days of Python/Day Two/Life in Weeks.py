# day 2 life in weeks project

#get age
userAge = input("What is your current age? ")

#calc total day weeks and months lives
userDaysLived = int(userAge) * 365
userWeeksLived = int(userAge) * 52
userMonthsLived = int(userAge) * 12


#total age assumption
year_calc = 90 - int(userAge)

#calc total day weeks and months left
userDaysLeft = year_calc * 365
userWeeksLeft = year_calc * 52
userMonthsLeft = year_calc * 12

#print days weeks months lived
print(f"You have lived {userDaysLived} days, {userWeeksLived} weeks and {userMonthsLived} months. ")

#print days weeks months left
print(f"You have {userDaysLeft} days, {userWeeksLeft} weeks and {userMonthsLeft} months left. ")