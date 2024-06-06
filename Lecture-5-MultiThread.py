import threading

def print_hello():
    print("Hello")


def print_goodbye():
    print("Goodbye")

thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_goodbye)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
