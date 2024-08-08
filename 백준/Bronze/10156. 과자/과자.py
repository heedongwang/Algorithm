a,b,c=map(int,input().split())
price=a*b
if price<=c:
    print(0)
else:
    print(price-c)