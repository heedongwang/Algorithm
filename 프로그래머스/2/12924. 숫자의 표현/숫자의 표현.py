def solution(n):
    answer = 0
    cnt=0

    for i in range(1, n+1):
        cnt += i
        if n - cnt<0: 
            break
        if (n - cnt) % i == 0:
            answer += 1
            
    
    return answer