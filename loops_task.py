dictionary = {}
item = ""
total = 0


while  item != "done":
	item = input('item (enter "done" when finished): ')
	if item!="done":
		price = input('price:  ')
		quantity = input('quantity:  ')
		dictionary[item] = [price, quantity]

print ("""---------------
receipt
---------------""")

for item in dictionary:
	print (dictionary[item][1] + " " + item + " " + str(float(dictionary[item][0])*float(dictionary[item][1])) + "KD")
	total += (float(dictionary[item][0]) * float(dictionary[item][1]))

print("---------------")
print ("total: " + str(total) + "KD")