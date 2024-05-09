'''Countdown to a special event of your choice'''

import datetime
import threading
import time

def get_time_until(target_date):
    now = datetime.datetime.now()
    time_until = target_date - now
    return time_until

def display_countdown(target_date):
    while True:
        time_until = get_time_until(target_date)
        if time_until.total_seconds() <= 0:
            print("Countdown is over!")
            break

        days = time_until.days
        hours, remainder = divmod(time_until.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time until {target_date}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        time.sleep(1)

def main():
    # Set target date here
    target_date = datetime.datetime(2024, 10, 4, 13, 59, 59)

    # Schedule the display countdown function to be called every second
    threading.Thread(target=display_countdown, args=(target_date,), daemon=True).start()

    

if __name__ == "__main__":
    main()

