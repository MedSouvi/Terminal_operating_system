

def get_power(number, power):
    result = 1
    for _ in range(power):
        result *= number
    return result



print("|Welcome to the calculator app|\n")

while True:
    try:
        num1 = int(input("Enter the first number: "))

    except ValueError:
        print("this is not a nomber")

    else:
        break


operation = input("Choose an operation(+, -, x, /, or click for power, or space for racin): ")

while True:
    try:
        num2 = int(input("Enter the second number: "))

    except ValueError:
        print("this is not a nomber")

    else:
        break


if operation in ("+", "-", "*", "x", "/", "", " "):

    if operation == "+":
        print(f"{num1} + {num2} = {num1+num2}")

    elif operation == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    
    elif operation in ("*", "x", "X"):
        print(f"{num1} {operation} {num2} = {num1*num2}")
    
    elif operation == "":
        print(f"{num1} power of {num2} = {get_power(num1, num2)}")

else:
    print(f"invalid operation: {operation}")
