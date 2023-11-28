def game(number):
    import math
    x = number % 10
    y = math.floor(number/10)
    return abs(x-y)
