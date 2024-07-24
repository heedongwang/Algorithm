
while True:
    a,b,c=map(int,input().split())
    li=[a,b,c]
    maxi=max(li)
    if a==b==c==0:
        break
    if a==b==c:
        print('Equilateral')
        
    elif maxi<(sum(li)-maxi):
        if a==b or b==c or a==c:
            print('Isosceles ')
            
        else:
            print('Scalene')
            
    else:
        print('Invalid')
        