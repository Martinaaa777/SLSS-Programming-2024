# martina panosetti
# 22 february


# ask the user if he wants fries with the meal
fries = input ("would you like fries with your meal?") #Yes

if fries.lower().strip("!") == "yes":
      print ("here there are, bye!")
elif fries.lower().strip("!") == "no":
      print (f"no worries, enjoy your meal!")
else: 
       print (f"sorry, i don't understand {fries}")