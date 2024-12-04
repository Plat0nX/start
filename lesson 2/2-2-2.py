n = 0
height = int(input("Enter your desired height"))
material = "*"
space = " "
while n < height:
    print(space*(height-n),2*n*material)
    n = n+1