a = float(input("Enter 1st number"))
b = float(input("Enter 2nd number"))
c = float(input("Enter 3rd number"))
if a < b and a < c:
    print (a,"1st number is the smallest")
elif b < a and b < c:
    print (b,"2nd number is the smallest")
elif c < a and c < b:
    print (c,"3rd number is the smallest")
else:
    print ("The smallest numbers are equal")