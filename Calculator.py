



print("Whilst using this calculator you write a number then write an operator then your last number. For the operator + = addition, - = subtraction, * = multiplication, / = division")




while True:
    num1 = float(input("Enter first number: "))
    op = (input("Enter operator: "))
    num2 = float(input("Enter second number: "))


    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid Operator")

    again = input("Would you like to use the calculator again: Yes/No\n")
    againn = again.lower()
    if againn == "yes":
        continue
    elif againn == "no":
        break
    else:
        break
