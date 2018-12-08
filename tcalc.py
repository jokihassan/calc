# Program make a simple calculator that can add, subtract, multiply and divide using functions
print(f"Select operation.")
print(f"1.+")
print(f"2.-")
print(f"3.*")
print(f"4./")

# Take input from the user
choice = input("Enter choice( +, -. *,  / ):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def switch_op(operator, x, y):
   return {
      "+": x + y,
      "-": x - y,
      "*": x * y,
      "/": x / y
   }.get(operator, "Please select a valid operator")


print(f"{num1} {choice} {num2} = {switch_op(choice,num1,num2)}")

