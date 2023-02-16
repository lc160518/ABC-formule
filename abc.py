import math

done = False
ABC = []


def ask_input():
    a = input("a= ")
    b = input("b= ")
    c = input("c= ")

    ABC.append(a)
    ABC.append(b)
    ABC.append(c)

    convert_input(a, b, c)


def convert_input(a, b, c):

    for i in range(0, len(ABC)):
        if "," ABC[i]

    a = int(a)
    b = int(b)
    c = int(c)

    positive_x(a, b, c)
    negative_x(a, b, c)

def positive_x(a, b, c):
    ans1 = (-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(ans1)


def negative_x(a, b, c):
    ans2 = (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(ans2)


while not done:
    ask_input()
    print("")
