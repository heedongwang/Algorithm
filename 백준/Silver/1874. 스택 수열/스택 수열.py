maxnum=int(input())   
li=[int(input()) for _ in range(maxnum)]
stack=[]
result=[]
count=1
check = True
for i in li:
    while count<=i:
        stack.append(count)
        result.append("+")
        count+=1
    
    if stack[-1]==i:
        stack.pop()
        result.append("-")
    else:
        check=False
        break        


if check:
    for i in result:
        print(i)
    
else:
    print("NO")

    
    