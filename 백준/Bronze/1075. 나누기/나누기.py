n=input()
f=int(input())
n=n[:-2]

for i in range(0,100):
    i= str(i)
    if int(i)<10:
        i='0'+i
        n1=n+i
    else:
        n1=n+i

    if int(n1)%f==0:
        print(i)
        break
