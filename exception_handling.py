try:
    n=0
    num = 8
    result = num / n
except (ZeroDivisionError) as e: # custom variable it contains python official explaination
    print("error",e)
except ValueError:
    print("entrer right value")

else:
    print(result)
finally:
    print("always executed")


D = {"KEY1":"VALUE1"}
try:
    val = D['KEY2']
except KeyError as e:
    print("NOT FOUND",e)