import math
import re

global x
global y
global z
z = 0

print("Enter a calc: ")
y = str(input(""))

for i in range(len(y)):
    try:
        if "+" in y:
            y = [int(num.strip()) for num in re.split(r"\+", y)]
            print("sum : ", sum(y))
        elif "-" in y:
            y = [int(num) for num in re.findall(r"[+-]?\d+", y)]
            print("sum : ", sum(y))
        elif "*" in y:
            y = [int(num.strip()) for num in re.split(r"\*", y)]
            # y = [int(item.strip()) for item in y]
            # print(y)
            # y[i] = int(y[i - 1]) * int(y[i + 1])
            # y.remove(y[i + 1])
            prod = y[0]
            for n in y[1:]:
                prod *= n
            print(y)
            print("sum : ", sum(y))
        elif "sin" in y:
            print("there is a sin")
            # y = [s.replace(f"sin({z})", "") for s in y]
            print(y)
            # assign the float to a var and then change to str for replace
            # y = [s.replace("sin()", math.sin(x)) for s in y]
    except ValueError as err:
        print(y)
        print(f"Invalid numbers: {err}")
