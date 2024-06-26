list=[]
for i in range(9):
    list.append(int(input()))

max= list[0]
for i in list:
    if max<i:
        max=i
        
print(max)
print(list.index(max)+1)