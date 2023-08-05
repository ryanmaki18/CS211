# Timer that tacks how long it takes to run specific function
# Practice with decorators (@)
# Created on February 10, 2023

import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write(f"Called function with " + "".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper

@log
def run(a, b, c = 9):
    print(a+b+c)

run(1, 9, c = 9)
