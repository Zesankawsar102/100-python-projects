import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Fuck OFF!")

print("How many seconds to count down? Enter an Number:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an Number! Enter an Number:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)