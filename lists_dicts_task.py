skills = ['work under pressure','work in a team', 'work with opposite gender', 'work with same gender', 'work from home', 'work during war']

cv = {}
cv['name'] = input("What is your name?  ")
cv['age'] = input("How old are you?  ")
cv['experience'] = input("How many years of experience you have?  ")
cv['skills'] = []

skill_number = 1
for skill in skills:
	print(str(skill_number) + "- " + skill)
	skill_number += 1


skill_choice1 = input("Please choose skill number of your choice:  ")
skill_choice2 = input("Please choice another skill number of your choice:  ")

cv['skills'].append(skills[int(skill_choice1)-1])
cv['skills'].append(skills[int(skill_choice2)-1])

if (int(cv['experience']) <= 2) and ('work with opposite gender' in cv['skills']) and ('work during war' in cv['skills']):
	print("Congratulations, " + cv['name'] + ", you are now officially one of us!")
else:
	print("Sorry, "+ cv['name'] + ", it seems like you don't belong here!")


