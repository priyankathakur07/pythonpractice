a = int(input("enter A"))
b = int(input("enter B"))
c = input("enter operation you want to perform, +,-,*,% ")
if c == "+":
    sum = a+b
    print(sum)
elif c == "-":
    sub = a-b
    print(sub)
elif c == "*":
    mult = a*b
    print(mult)
elif c == '%':
    rem = a % b
    print(rem)
else:
    print("invalid operationns")
