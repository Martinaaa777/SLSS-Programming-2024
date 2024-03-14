# conditionals
# martina panosetti
15-02-2024

# implement the flowchart from notes
x = 1_000_000
y = -5.7

# if x is less than y, say so
# if x is greater than y, say so
# if x is equal to y, say so

if x < y:
    print ("x is less than y")
if x > y:
    print ("x is greater than y")
if y == y :
    print ("x is equal to y")

if x < y:
    print ("x is less than y")
 elif x > y: 
    print ("x is greater than y")
else:
    print ("x is equal to y")

foo = int (input ("enter a number:"))  #string

if foo < -1 or foo == 0 :
    print ("foo is less than 1")
    print ("or it is equal to 0")

 # check if foo is inside a range
 # greater than 1 and less than 1000
if foo > 1 and foo < 1000: 
    print ("foo is in the range 2 - 999")
else:
    print ("foo is outside the range 2 - 999")
    