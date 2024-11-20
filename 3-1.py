a = float(input("Введите первое число"))
b = float(input("Введите второе число"))
print ("Предложенные операции: plus or +, div or /, minus or -, multiply or *, mod or %, power or **, div2 or //")
c = str(input("Какую операцию вы хотите совершить?"))
if c == "plus" or c == "+":
    print(a+b)
elif c == "div" or c == "/":
    print(a/b)
elif c == "minus" or c == "-" :
    print(a-b)
elif c == "multiply" or c == "*":
    print:(a*b)
elif c == "mod" or c == "%":
    print(a%b)
elif c == "power" or c == "**":
    print(a**b)
elif c == "div2" or c == "//":
    print(a//b)