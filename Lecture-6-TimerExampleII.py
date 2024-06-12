# Import the threading module
import threading

# Define a function that will be called by the timer
def remind_break():
    print("Time to take a break!")

# Create a timer that will call the remind_break function after 3600 seconds (1 hour)
# The first argument is the time in seconds
# The second argument is the function to be called
break_timer = threading.Timer(3600, remind_break)

# Start the timer
break_timer.start()

# Optional: If you want to cancel the timer before it finishes
# break_timer.cancel()
