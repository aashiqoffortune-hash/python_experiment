a = float(input("Give me a number: "))
b = input("Give me a operator: ")
x = float(input("Give me yet another number: "))

if b == "+":
    print(a + x)
elif b == "-":
    print(a - x)
elif b == "*":
    print(a * x)
elif b == "**":
    print(a**x)
elif b == "/":
    print(a / x)
else:
    print("Unknown operator.")
