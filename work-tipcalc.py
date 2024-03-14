# Tip Calc
# Author: martina panosetti
# 29 feb 2024

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")



    # Converts string dollars to a decimal float
    #    Returns the result
    # TODO

def dollars_to_float (d: str):
    # Converts string dollars to a decimal float
    #    Returns the result
    return float(d)



    # Converts percent to a decimal float
    #    Returns the result
    # TODO

def percent_to_float(p):
# Converts percent to a decimal float
    #    Returns the result
    return float(p) / 100

main()