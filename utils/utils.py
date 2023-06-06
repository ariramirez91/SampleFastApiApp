import math

def is_perfect_square(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def is_fibonacci_number(num):
    if is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4):
        return True
    return False


def fibonnacci(givenNumber):
    number1 = 1
    number2 = 1
    nextFibo = number1 + number2
    while nextFibo <= givenNumber:
        number1 = number2
        number2 = nextFibo
        nextFibo = number1 + number2

    return nextFibo
