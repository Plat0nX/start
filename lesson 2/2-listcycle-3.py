lst =[989,422,674,411,867,213,757,787,134,900]
value = lst[0]
for i in lst:
    if value > i:
        value = i
print(value)
for i in lst:
    if value < i:
        value = i
print(value)