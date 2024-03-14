# martina panosetti
# 04 march 2024

# create a function that can convert a euro value in a dollar value 
# the function returns the converted value
def convert_amount (amount):
    converted_amount= amount
    return converted_amount

# the function will ask to put the amount in euro
def euro ():      
    return input ("enter the amount in euro")


#the function will show the amount in canadian dollars
def result (amount_euro):
    cad = amount_euro * 1.47

    return cad

# the function makes everything work
    # the function checks the validity of the amount of money 
def main ():
    amount_euro = float(euro())

    # If the person says anything less than zero, ask them again
    # Also ask them again if it's greater than 10000
    while amount_euro < 0 or amount_euro > 10_000:
        if amount_euro >10_000:
            print ("the amount is too high. please enter another one")
        else:
            print ("invalid amount. please enter a valid one")
        
        amount_euro = float(euro ())
    
    amount_cad = result(amount_euro)
    print(f"the amount in CAD is {amount_cad}")


main()