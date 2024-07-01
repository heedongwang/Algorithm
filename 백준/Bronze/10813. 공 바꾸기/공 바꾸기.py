n,m=map(int, input().split())
li=[]
for i in range(1,n+1):
    li.append(i)

for i in range(m):
    a,b= map(int, input().split())
    temp= li[a-1]
    li[a-1]=li[b-1]
    li[b-1]=temp

for i in li:
    print(i,end=" ")