import math

done = False


def positive_x(a, b, c):
    ans1 = (-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(ans1)


def negative_x(a, b, c):
    ans2 = (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(ans2)


while not done:
    a = int(input("a= "))
    b = int(input("b= "))
    c = int(input("c= "))

    positive_x(a, b, c)
    negative_x(a, b, c)
    print("")


