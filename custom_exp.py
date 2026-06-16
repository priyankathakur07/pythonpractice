# define exception
class invalid_amount(Exception):
    def __init__(self, amount):
        super().__init__(f"cant process {amount}")
def deposit(amount):
    if amount <=0:
        raise invalid_amount(amount)
        print(f"{amount} succesfully deposited")

try:
    deposit(-90)
except invalid_amount as e:
    print("invalid")