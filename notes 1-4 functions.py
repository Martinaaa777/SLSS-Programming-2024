# functions
# martina panosetti
# 26 feb 2024


# create a function called say_hello
# it is going to print hello
def say_hello():
    print ("hello!")


# create a function called say_hello_params
    print ("hello {parameter!}")
def say_hello_params(name):
    print (f"hello{name}")


# create a function called how_big
# it takes a number as an input-param
    # it returns how big the number is
def how_big (num) :
    if num<0: 
        return "very small"
    if num <10:
        return "pretty small"
    if num <100:
        return "small"
    if num <1000:
        return "pretty big"
    return "really big"


# create a function called adder
#    accepts two inputs that are numbers
#    retur the SUM of both numbers
def adder (x: int,y:int):
    return x+y


say_hello()
say_hello_params ("Jim")

print (how_big (-1))
print (how_big (1))
result = how_big (1_000_000)
print (result)

result = adder (1,1) #2
print (result)
result = adder (100,123)
print (result)
