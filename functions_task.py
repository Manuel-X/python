from datetime import datetime
now = datetime.now()

def check_birthdate(entered_year,entered_month,entered_day):
	if entered_year > now.year:
		return False
	elif (entered_year == now.year) and (entered_month > now.month):
		return False
	elif (entered_year == now.year) and (entered_month == now.month) and (entered_day > now.day):
		return False
	else:
		return True

def calculate_age(entered_year,entered_month,entered_day):
	month_temporary=now.month
	year_temporary=now.year

	if now.year % 4 == 0:
		year_type = "leap year"
	else:
		year_type = "normal year"

	if now.month == 1 or now.month == 3 or now.month == 5 or now.month == 7 or now.month == 8 or now.month == 10 or now.month== 12:
		current_month_days = 31
	elif now.month == "4" or now.month == "6" or now.month == "9" or now.month == "11":
		current_month_days = 30
	elif now.month == "2" and year_type == "leap year":
		current_month_days = 29
	elif now.month == "2" and year_type == "normal year":
		current_month_days = 28

	if now.day > entered_day: 
		no_of_days = now.day - entered_day
	else:
		month_temporary -= 1
		no_of_days =  (now.day + current_month_days) - entered_day

	if month_temporary > entered_month:
		no_of_months = month_temporary - entered_month
	else:
		year_temporary -= 1
		no_of_months = (month_temporary + 12) - entered_month

	no_of_years = year_temporary - entered_year
	print ("Your age is: {} years, {} months and {} days".format(no_of_years,no_of_months,no_of_days))


user_year = int(input("Enter year:  "))
user_month = int(input("Enter month:  "))
user_day = int(input("Enter day:  "))

if check_birthdate(user_year,user_month,user_day):
	calculate_age(user_year,user_month,user_day)
else:
	print ("Birthdate is invalid")
