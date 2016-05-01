import sys

if len(sys.argv) > 1:
    y = sys.argv[1]
else: 
    y = input("Please enter a number: ")

while True:
    try:  
        int(y)
        break
    except ValueError:
        print("That's not a number!")
        y = input("Please enter a new number. ") 

y = int(y)

x = 1

while x <= y:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print (x)
    
    x += 1