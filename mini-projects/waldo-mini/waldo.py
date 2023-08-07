# Mini-Project - Week 4
# CS 211, Winter 2023
# Ryan Maki


Waldo = 'W'
Other = '.'


def all_row_exists_waldo(matrix: list[str]) -> bool:
    for row in range(len(matrix)):
        if Waldo not in matrix[row]:
            return False
    return True


def all_col_exists_waldo(matrix: list[str]) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return True
    for col in range(len(matrix[0])):
        maybe_waldo = False
        for row in range(len(matrix)):
            if matrix[row][col] == Waldo:
                maybe_waldo = True
                break
        if not maybe_waldo:
            return False
    return True


def all_row_all_waldo(matrix: list[str]) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return True
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != Waldo:
                return False
    return True


def all_col_all_waldo(matrix: list[str]) -> bool:  # Redundant (Another example of what we can se below)
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return True
    for col in range(len(matrix[0])):
        maybe_waldo = True
        for row in range(len(matrix)):
            if matrix[row][col] != Waldo:
                maybe_waldo = False
                break
        if not maybe_waldo:
            return False
    return True


# def all_col_all_waldo(matrix: list[str]) -> bool:  # Redundant
#     return all_row_all_waldo(matrix)


def exists_row_all_waldo(matrix: list[str]) -> bool:
    for row in range(len(matrix)):
        maybe_waldo = 0
        for col in range(len(matrix[0])):
            if matrix[row][col] != Waldo:
                break
            maybe_waldo += 1
        if maybe_waldo == len(matrix[row]):
            return True
    return False


def exists_col_all_waldo(matrix: list[str]) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    for col in range(len(matrix[0])):
        maybe_waldo = 0
        for row in range(len(matrix)):
            if matrix[row][col] != Waldo:
                break
            maybe_waldo += 1
        if maybe_waldo == len(matrix[0]):
            return True
    return False


def exists_row_exists_waldo(matrix: list[str]) -> bool:
    for row in range(len(matrix)):
        if Waldo in matrix[row]:
            return True
    return False


def exists_col_exists_waldo(matrix: list[str]) -> bool:  # Redundant
    return exists_row_exists_waldo(matrix)

