import math

global x
global y
global z2
global ask
global getAnswer
global tan
global sin
global cos
global oper1
oper1 = ""


def init():
    print("+,-,*,/,T(an),S(in),C(os) : ")
    oper1 = str(input(""))
    return oper1


def basic(oper1):
    if "T" in oper1:
        print("Tangent Of : ")
        tan = float(input(""))
        print(f"trig ans : ", math.tan(tan))
    elif "S" in oper1:
        print("Sine Of : ")
        sin = float(input(""))
        print(f"trig ans : ", math.sin(sin))
    elif "C" in oper1:
        print("Cosine Of : ")
        cos = float(input(""))
        print(f"trig ans : ", math.cos(cos))


# make it so that the user can put more inputs than just two


def regCalc(oper1):
    if "+" in oper1:
        x = int(input("num1 : "))
        y = int(input("num2 : "))
        z2 = x + y
        print(f"ans : {z2}")
    elif "-" in oper1:
        x = int(input("num1 : "))
        y = int(input("num2 : "))
        z2 = x - y
        print(f"ans : {z2}")
    elif "*" in oper1:
        x = int(input("num1 : "))
        y = int(input("num2 : "))
        z2 = x * y
        print(f"ans : {z2}")
    elif "/" in oper1:
        x = int(input("num1 : "))
        y = int(input("num2 : "))
        z2 = x / y
        print(f"ans : {z2}")
        if x < y:
            z2 = x / y
            z2 = float(z2)
            print(f"ans : {z2}")
        elif x >= y:
            z2 = x / y
            z2 = int(z2)
            print(f"ans : {z2}")


def runner(oper1):
    oper1 = init()
    basic(oper1)
    regCalc(oper1)
    redo()


def redo():
    print("More? (Y/n) :")
    ask = str(input(""))
    if "Y" in ask:
        runner(oper1)
    elif "y" in ask:
        runner(oper1)
    elif "n" in ask:
        print("Ending")
        exit()
    elif "N" in ask:
        print("Ending")
        exit()
    else:
        print("Invalid")
        redo()


runner(oper1)
