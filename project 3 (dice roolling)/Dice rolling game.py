import random

def dice_rolling():
    
    while True:
        print('''1.roll the dice''')
        print('''2.To exit''')
        user = int(input("what you want to do\n"))
        if user==1:
            number = random.randint(1,6)
            print(number)
        else:
            print("Thanks")
            break
            
dice_rolling()
