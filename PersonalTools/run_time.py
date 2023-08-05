# Timer that tacks how long it takes to run specific function
# Practice with decorators (@)
# Created on February 10, 2023

import time


def timer(func):
    """
    Decorator for measuring function's running time.
    """
    def wrapper():
        before = time.time()
        func()
        print(f"Function Took: {time.time() - before} seconds.")

    return wrapper


@timer
def run():
    time.sleep(2)


if __name__ == "__main__":
    run()
