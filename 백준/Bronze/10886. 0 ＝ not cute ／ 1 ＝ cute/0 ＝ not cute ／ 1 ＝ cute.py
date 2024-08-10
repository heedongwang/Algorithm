n=int(input())
cu,no=0,0
for i in range(n):
    cute=int(input())
    if cute==1:
        cu+=1
    else:
        no+=1
if cu>no:
    print("Junhee is cute!")
else:
    print( "Junhee is not cute!")