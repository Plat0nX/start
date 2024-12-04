a = int(input("Введите сторону a"))
b = int(input("Введите сторону b"))
c = int(input("Введите сторону c"))
m = int(input("Ширина проема"))
k = int(input("Высота проема"))
if a < m and b < k:
    print("Box is going through")
elif a < m and c < k:
        print("Box is going through")
elif b < m and a < k:
    print("Box is going through")
elif b < m and c < k:
    print("Box is going through")
elif b < m and c < k:
    print("Box is going through")
elif c < m and a < k:
    print("Box is going through")
elif c < m and b < k:
    print("Box is going through")
else:
    print("ne vlezlo")
