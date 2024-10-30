import threading


def print_hello():
    print("Hello")
    for i in range(1, 200):
        print(f"COMING FROM PRINT_HELLO: The value for i is:  {i} \n")


def print_goodbye():
    for j in range(1000, 2000):
        print(f"COMING FROM PRINT_GOODBYE: The value for j is:  {j} \n")
    print("Goodbye")


thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_goodbye)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
