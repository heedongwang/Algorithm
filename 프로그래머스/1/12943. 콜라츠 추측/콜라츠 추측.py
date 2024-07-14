def solution(num):
    answer = 0
    count=0
    while num>=1:
        if num==1:
            return 0
            break
        if num%2==0:
            num/=2
            count+=1
        else:
            num*=3
            num+=1
            count+=1
        if num!=1 and count>=500:
            return -1
            break 
            
        elif num==1 and count<=500:
            return count
            break
            
        
