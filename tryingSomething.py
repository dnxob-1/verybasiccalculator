import math

print("Enter a calc: ")
x = str(input(""))


if "+" in x:
    print(True)
    y = x.split()  # split on + so you can find the ints and then add or such
    print(y)
    for i in y:
        if isinstance(i, int):
            print("There is a num")
else:
    print(False)
