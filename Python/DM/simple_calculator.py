a = int(input("Enter the first input: "))
b = int(input("Enter the second input: "))

operator = input("Enter the operation: ")
if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
else:
    print("Incorrect operator")
