#탐욕알고리즘
n=int(input())
weight=[5,3]
suger=0

while n>0:
    if n%5==0:
        suger+=(n//5)
        print(suger)
        break
    else:
        n=n-3
        suger+=1
        if n%5==0:
            suger+=(n//5)
            print(suger)
            break
        elif n==1 or n==2:
            print(-1)
            break
        elif n==0:
            print(suger)
            break
