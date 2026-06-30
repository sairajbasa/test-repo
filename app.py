# cake_check.py

import time
import random

cake_ready = False
minutes_waited = 0

# Random baking time between 3 and 7 minutes
baking_time = random.randint(3, 7)

print(f"The cake will take about {baking_time} minutes to bake...")

while not cake_ready:
    print(f"Waiting... {minutes_waited} minutes passed.")
    time.sleep(1)   # pretend 1 second = 1 minute
    minutes_waited += 1

    if minutes_waited >= baking_time:
        cake_ready = True

if cake_ready:
    print("Yay! The cake is ready. Let's eat!")


