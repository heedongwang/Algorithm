tcase=int(input())
li=[]
for i in range(tcase):
    a,b=map(int, input().split())
    if a%10==0:
        print(10)
    else:
        b=b%4+4
        print((a**b)%10)