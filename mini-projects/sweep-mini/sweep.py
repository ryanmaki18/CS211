# Mini-project: List Sweep Algorithms
# Ryan Maki
# CS 211 @ 10:00 Tues/Thurs
# Got help from an LA


def all_same(l: list) -> bool:
    """A function that determines whether all the elements in a list are the same"""
    if len(l) == 0:
        return True
    elem = l[0]
    for item in l:
        if item != elem:
            return False
    return True


# assert all_same([1, 1, 1, 1]) == True
# assert all_same([]) == True
# assert all_same([1, 3, 1, 1]) == False


def dedup(l: list) -> list:
    """A function that returns a de-duplicated version of the input list."""
    result = []
    if len(l) == 0:
        # returns an empty list if length of l is 0
        return result
    curr_run = l[0]
    result.append(curr_run)
    for i in range(1, len(l)):
        if l[i] != l[i-1]:
            result.append(l[i])
    return result


# assert dedup([]) == []
# assert dedup([1, 1, 2, 1, 1]) == [1, 2, 1]


def max_run(l: list) -> int:
    """A run is a subsequence with identical values."""
    if len(l) == 0:
        return 0
    curr_run = None
    curr_len = 1
    longest_len = 1
    for item in l:
        if item == curr_run:
            curr_len += 1
            if curr_len >= longest_len:
                longest_len = curr_len
        else:
            curr_run = item
            curr_len = 1
    return longest_len
help(max_run)

# assert max_run([1, 1, 2, 2, 3, 4, 4, 4, 2, 4, 4]) == 3.
# assert max_run([]) == 0
# assert max_run([1, 2, 3]) == 1
# assert max_run([1, 2, 1, 1]) == 2.
