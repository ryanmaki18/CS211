# Tracks time that it takes program to run (we made multiple progrms and found fasted way)
# Created on February 10, 2023


"""First Attempt"""
# import time
# import random
#
# our_list = list(range(10000000))
# element = 7000000
#
# start = time.time()
#
# random_choice = random.choice(our_list)
# while random_choice != element:
#     random_choice = random.choice(our_list)
#
# end = time.time()
#
# print(end - start)


"""Second Attempt"""
# import time
#
# our_list = list(range(10000000))
# element = 7000000
#
# start = time.time()
#
# for el in our_list:
#     if el == element:
#         break
#
# end = time.time()
#
# print(end - start)


"""Third Attempt"""
# Used binary_search.py
# This is the fastest algorithm

import time
from binary_search import binary_searcher

our_list = list(range(10000000))
element = 700000

start = time.time()

binary_searcher(our_list, element)

end = time.time()

print(f"Function Took: {end - start} seconds")





