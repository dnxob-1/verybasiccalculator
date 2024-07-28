import math

global x
global y
global z2
global ask
global getAnswer
global tan
global sin
global cos

def basic():
    print("+,-,*,/,T(an),S(in),C(os) : ")
    operation = str(input(""))
    if 'T' in operation:
        print("Tangent Of : ")
        x = None
        y = None
    elif 'S' in operation:
        print("Sine Of : ")
        x = None
        y = None
    elif 'C' in operation:
        print("Cosine Of : ")
        x = None
        y = None
    else:
        x = int(input("num1 : "))
        y = int(input("num2 : "))
    return x , y , operation

def calc():
    x,y,operation = basic()
    if '+' in operation:
        z2 = x + y
    elif '-' in operation:
        z2 = x - y
    elif '*' in operation:
        z2 = x * y
    elif '/' in operation:
        z2 = x / y
        if x < y:
            z2 = x / y
            z2 = float(z2)
        elif x >= y:
            z2 = x / y
            z2 = int(z2)
    elif 'T' in operation:
        tan = float(input(""))
        print(f"trig ans : ", math.tan(tan))
        z2 = None
    elif 'S' in operation:
        sin = float(input(""))
        print(f"trig ans : ", math.sin(sin))
        z2 = None
    elif 'C' in operation:
        cos = float(input(""))
        print(f"trig ans : ", math.cos(cos))
        z2 = None
    else:
        print("Invalid Notation")
        calc()
    print(f"ans : {z2}")
    redo()

def redo():
    print("More? (Y/n)")
    ask = str(input(""))
    if 'Y' in ask:
        calc()
    elif 'n' in ask:
        print("Ending")
        exit()
    else:
        print("Invalid")
        redo()
calc()
