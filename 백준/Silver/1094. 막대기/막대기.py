x=int(input())

#처음 막대 길이
origin=64


li=[origin]

while True: 
   
    if x<sum(li):
        li.sort()
        min=li[0]
        
        #최단 막대기 삭제
        li.remove(min)
        
        #최단 막대기를 두개로 나눔
        li.append(min//2)
        
        #막대의 붙였을때 길이 충족여부
        if sum(li)<x:
            li.append(min//2)
    else:
        break

print(len(li))

        
        
    
    