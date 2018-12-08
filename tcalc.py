# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def sub(x, y):
   return x - y

# This function multiplies two numbers
def mul(x, y):
   return x * y

# This function divides two numbers
def div(x, y):
   return x / y

print(f"Select operation.")
print(f"1.Add")
print(f"2.Sub")
print(f"3.Mul")
print(f"4.Div")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def switch_op(operator, x, y):
   return {
   'add': lambda: x + y,
   'sub': lambda: x - y,
   'mul': lambda: x * y,
   'div': lambda: x / y
   }.get(operator, lambda: None)()
