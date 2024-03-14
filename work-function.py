# martina panosetti
# 27 feb 2024
# functions

# create a function called replacer
# accepts a string
# replace 100 with 💯
# replace all noodles with 🍝
# return the result

def translate(usr_input):
    # Your block of code goes in here
    # Delete the pass and put in your own code
    return usr_input.replace("100", "💯").replace("noodles", "🍜") 


# create a function called main
# prompt the user to type
# use the translate function on the user input
# print the result input
def main ():
 # Get the user's input
    usr_input = input()
    # Use the translate function on the
    #    user's input
    print(translate(usr_input)) 

# testing happens outside the function 
    #


