def calculator():
    print("Operation: +,-,*,/,//,**,%")
    operation = input("choose operation: ")
    num1 = float(input("Enter first nunber: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
       print(num1 + num2)
    elif operation == "-":
       print(num1 - num2)
    elif operation == "*":
       print(num1 * num2)
    elif operation == "/":
       if num2 != 0:
           print(num1 / num2)
       else:
           print("Cannot divide by zero!")
    elif operation == "//":
       if num2 != 0:
           print(num1 // num2)
       else:
           print("Cannot divide by zero!")
    elif operation == "**":
        print(num1 ** num2)
    elif operation == "%":
        print(num1 % num2)
    else:
       print("Invalid operation!")

calculator()