from collections import Counter
def solution(k, tangerine):
    answer = 1
    maxadd=0
    
    li=list(Counter(tangerine).values())
    li.sort(reverse=True)
    
    for i in range(len(li)):
        maxadd+=li[i]
        if maxadd>=k:
            return answer
        answer+=1
    print(li)
    return answer