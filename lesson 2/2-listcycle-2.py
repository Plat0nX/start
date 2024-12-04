lst =[141,422,674,411,867,213,757,787,989,900]
print(sum(lst))
s=0
for i in lst:
    if i%2 == 0:
        s=s+i
print(s)