import math

def if_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# take user input
num = int(input("Enter a number: "))
if if_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")