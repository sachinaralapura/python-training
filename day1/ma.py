import math


def factorial(n):
    """
    This is  a factorial function
    factorial(positive number)

    """
    if n < 0:
        return "enter positive number"
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# function for finding roots
def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print("real and different roots")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print("real and same roots")
        print(-b / (2 * a))

    # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(-b / (2 * a), +i, sqrt_val)
        print(-b / (2 * a), -i, sqrt_val)


def sum_of_numbers(n):
    """
    this give the sum of first 'n' numbers
    sum_of_number(int:n):int
    """
    sum = 0
    for i in range(n):
        sum += i
    return sum


a = {2023, "Python", 3.11, 5 + 6j, 1.23e-4, "Python"}
# b = {(5 + 6j), 3.11, 0.000123, "Python", 2023}
c = {1, 2, 3, 4, 5}

print(a)
