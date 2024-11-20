num = (int(input("Введите трехзначное число")))
a = num//100
b = (num-(a*100))//10
c = num-a*100-b*10
print (a, b, c)
if a == b == c:
    print("Все цифры одинаковы")
elif num >= 1000 or num <= 0:
    print("Вы ввели неверное число")
elif a == b:
    print("1 и 2 цифры одинаковые")
elif c == b:
    print("2 и 3 цифры одинаковые")