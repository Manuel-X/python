from datetime import datetime
todays_date = datetime.now()
employee_list = []
manager_list = []

class Employee:

	def get_working_years (self):
		return todays_date.year - int(self.employment_date)

	def add_employee(self):
		self.name = input("name:  ")
		self.age = input("age:  ")
		self.salary = input("salary:  ")
		self.employment_date = input("employment_year:  ")


	def print_list(self):
		print ("Employees:")
		count = 0
		while count < len(employee_list):
			print ( "name: {}, age: {}, salary: {}, working_years: {}".format( employee_list[count],employee_list[count+1],employee_list[count+2],employee_list[count+3],manager_list[count+4] ))
			count += 4
		
		




class Manager(Employee):
	def __init__ (self):
		self.manager_list = []

	def get_working_years (self):
		super().get_working_years()

	def add_employee(self):
		super().add_employee()
		self.bonus_percentage = input("bonus_percentage:  ")

	def get_bonus(self):
		return float(self.bonus_percentage)*float(self.salary)

	def print_list(self):
		print ("Managers:")
		count = 0
		while count < len(manager_list):
			print ( "name: {}, age: {}, salary: {}, working_years: {}, bonus: {}".format( manager_list[count],manager_list[count+1],manager_list[count+2],manager_list[count+3],manager_list[count+4]))
			count += 5

choice = "0"
while choice != "5":
	print ("""
	Welcome to HR Pro 2019
	Choose an action to do:
	1. show employees
	2. show managers
	3. add an employee
	4. add a manager
	5. exit
	""")
	choice = input("what would you like to do?  ")

	if  choice == "1":
		print(new_employee.print_list())
	elif choice == "2":
		print (new_manager.print_list())
	elif choice == "3":
		new_employee = Employee()
		new_employee.add_employee()
		employee_list.extend([new_employee.name, new_employee.age, new_employee.salary, new_employee.get_working_years()])

	elif choice == "4":
		new_manager = Manager()
		new_manager.add_employee()
		manager_list.extend([new_manager.name, new_manager.age, new_manager.salary, new_manager.get_working_years(), new_manager.get_bonus()])



