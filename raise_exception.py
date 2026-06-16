def set(age):
    if age<0:
        raise ValueError("age cant negative")
    print({age})

try:
    set(-8)
except ValueError as e:
    print(e)