m = int(input("Введите сумму вклада"))
k = float(input("Введите процентную ставку без знака процента"))/100+1
s = int(input("Введите желаемую сумму"))
y = 0
while s>m:
    m=m*k
    y=y+1
print(y)