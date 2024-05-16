# loops
# martina panosetti
# 5 april 2024

# Print "something" 10 times
for _ in range(10):
    print("something")

# create a grocery list
# do something for each item in the list
grocery_list = [
    "blberry muffin",
    "potato chips",
    "foil",
    "orange juice",
    "rtx 4070 super",
    "cereal"
]

# for every item:
#      * {grocery item}
#      * {grocery item}
#      * {grocery item}
for item in grocery_list:
    # skip the rest of the list 
    # if we get to rtx 4070 super
    if item.lower () == "rtx 4070 super" :
        print ("i cannot buy it, it is expensive")
        break # stop looping
    print (f"*{item}")

# can you count using a for loop ?
# use a for loop to count to 100
for i in range (100):
    print (i+ 1)


#while loops are useful for input validation
# ask the user if they like ice cream
# if they don't answer yes or no repeat the question

user_answer = input ("do you like ice cream?")

while user_answer not in ["yes", "no", "yeah", "nah"]
user_answer= input ("seriously, do you like ice cream?")

if user_answer in ["yes" "yeah"]:
    print("nice , i love ice cream too")
