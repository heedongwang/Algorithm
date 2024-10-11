import sys
num=int(sys.stdin.readline())
count=[]
for i in range(num):
    money=int(sys.stdin.readline())
    if money !=0:
        count.append(money)
    else:
        if len(count)>0:
            del count[-1]
    
print(sum(count))
