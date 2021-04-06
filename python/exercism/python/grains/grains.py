def square(number):
    if number < 1 or number > 64:
        raise ValueError("Invalid square number")
    return 2**(number-1)


def total():
    return 2**64 - 1
