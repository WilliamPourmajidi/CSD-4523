import threading


def greet():
    print("Welcome to Lambton College!")


def orient():
    print("Welcome to Python programming!")


# Create a timer that executes the greet function after 5 seconds
# timer_1 = threading.Timer(8.0, greet)
# timer_1.start()  # Starts the timer
# timer_2 = threading.Timer(18.0, orient)
# timer_2.start()  # Starts the timer

# Below code is slightly more concurrent because timer1 and timer 2 are started at once
timer_1 = threading.Timer(8.0, greet)
timer_2 = threading.Timer(18.0, orient)

timer_1.start()  # Starts the timer
timer_2.start()  # Starts the timer

print("timer has started")
