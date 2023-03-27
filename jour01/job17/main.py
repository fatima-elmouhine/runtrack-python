
for i in range(101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz", i)
    elif i % 3 == 0:  
        print("Fizz",i)
    elif i % 5 == 0:
        print("Buzz", i)