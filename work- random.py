# Martina panosetti
# 11 March 2024
# functions

# create a function for sequence
# the function will find the result of a sequence of numbers

def calculate_sum (sequence):
    # the variable stores the sum
    total = 0

    # add the elemnt to the total sum
    for num in sequence: 
        total = + num
    # return the result
        return total
    
numbers = [1,2,3,4,5]
result = calculate_sum(numbers)
print ("sum of the sequence", result) 