num1 = float(input())
num2 = float(input())
operation = input()
if num2 == 0.0 and operation in ["mod", "div", "/"]:
    print("Division by 0!")
elif operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "mod":
    print(num1 % num2)
elif operation == "pow":
    print(num1 ** num2)
elif operation == "div":
    print(num1 // num2)
