cla=int(input())

li=list(map(int,input().split()))

li.sort()
ma = li.pop(-1)
li.append(ma)

sum=0
nw=[]
for i in li:
    nw.append((i/ma)*100)

for i in nw:
    sum+= i
mea= sum/len(nw)
print(round(mea,7))