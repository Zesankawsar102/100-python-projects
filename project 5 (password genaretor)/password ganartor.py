import random
def password_generator():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    lenght = int(input("Number of password:"))
    Password = ''
    for i in range(lenght): 
        Password += random.choice(chars)
    print (Password)
    finish = ("Here Your STRONGEST password\n Bye-_-")
    print(finish)
password_generator()