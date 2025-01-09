def solution(n):
    answer = 0
    a=str(format(n, 'b'))
    #print(a)
    cnt_a=a.count("1")
    #print(cnt_a)
    while True:
        n+=1
        #print(n)
        b=str(format(n, 'b'))
        #print(b)
        cnt_b=b.count("1")
        #print(cnt_b)
        if cnt_a==cnt_b:
            break
        
    
    
    return n