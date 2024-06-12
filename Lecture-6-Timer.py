import threading

def greet():
    print("Hello, World!")

# Create a timer that executes the greet function after 5 seconds
timer = threading.Timer(5.0, greet)
timer.start()  # Starts the timer

