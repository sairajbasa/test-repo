# cake_check.py

import time

cake_ready = False   # At first, the cake is not ready
minutes_waited = 0

while not cake_ready:
    print(f"Waiting... {minutes_waited} minutes passed.")
    time.sleep(1)   # pretend 1 second = 1 minute
    minutes_waited += 1

    if minutes_waited >= 5:   # after 5 minutes, cake is ready
        cake_ready = True

if cake_ready:
    print("Yay! The cake is ready. Let's eat!")

