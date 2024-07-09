
na=[]
count=0
for i in range(0,10):
   num=int(input())
   na.append(num%42)

na=set(na)

print(len(na))
        