import datetime
import time
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("Wake up! Alarm ringing!")
            playsound("alarm.mp3")  # Make sure this file exists
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_input = input("Set alarm time (HH:MM in 24-hour format): ")
    try:
        datetime.datetime.strptime(alarm_input, "%H:%M")  # Validate format
        set_alarm(alarm_input)
    except ValueError:
        print("Invalid time format. Please use HH:MM (24-hour format).")
