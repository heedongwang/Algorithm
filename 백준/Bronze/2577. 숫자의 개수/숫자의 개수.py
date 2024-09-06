a=int(input())
b=int(input())
c=int(input())

num=str(a*b*c)
li=list(num)
an=[]
count=0
for i in range(0,10):
    for j in num:
        if i==int(j):
            count+=1
    an.append(count)
    count=0

for i in an:
    print(int(i))