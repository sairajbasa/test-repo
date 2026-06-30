# A very simple program

# Imagine we are baking a cake
cake_ready = False   # At first, the cake is not ready

# We check if the cake is baked
if cake_ready:
    print("Yay! The cake is ready. Let's eat!")
else:
    print("Oops! The cake is not ready yet. Wait a little longer.")

# Added a small extra check
# Let's also check how many minutes we waited
minutes_waited = 30

if not cake_ready and minutes_waited > 20:
    print("We've already waited 30 minutes... maybe check the oven!")
