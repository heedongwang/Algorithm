def solution(k, m, score):
    score.sort()
    box=[]
    asum=0
    while True:
        if len(box)==m:
            asum+=(m*min(box))
            box=[]

        if len(score)==0:
            return asum
       
        box.append(score[-1])
        score.pop()


solution(3,4,[1, 2, 3, 1, 2, 3, 1])