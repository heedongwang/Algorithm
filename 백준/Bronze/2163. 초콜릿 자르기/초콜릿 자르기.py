n,m=map(int,input().split())
w=n*m
count=0
while w>1:
    if w==1:
        break
    w-=1
    count+=1
    

print(count)