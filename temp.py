temp = float(input("enter a temp"))
convert = input("enter a unit to convert , C/F")
if convert == "c":
    fahrenheit = (temp*9/5) + 32
    print(fahrenheit)
elif convert == "f":
    celsius = (temp-32)*5/9
    print(celsius)
else:
    print("invalid celsiusd")
