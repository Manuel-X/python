print (""" Mad libs where libs get Mad,
  Start Below:

  """)
time_desired = input ("time:  ")
items_name = input("items:  ")
name_desired = input("name:  ").title()
scream_desired = input("scream:  ").upper()
action_desired = input("action:  ")

full_story= """   It was %s o'clock when I heard a knock at the door.    
   I opened the door and there was a box full of %s with a note saying "From Mr. %s".    
   Just as I closed the door I heard a scream "%s.".     
   I froze in place and all I could do was %s.""" % (time_desired, items_name, name_desired, scream_desired, action_desired)

print (full_story)
