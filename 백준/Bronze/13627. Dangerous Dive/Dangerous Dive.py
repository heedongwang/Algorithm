n,r= map(int, input().split())
li=list(map(int,input().split()))
notre=[]
for i in range(1,n+1):
    if i not in li:
        notre.append(i)

if len(notre)==0:
    print("*")
else:
    for i in notre:
        print(i,end=" ")