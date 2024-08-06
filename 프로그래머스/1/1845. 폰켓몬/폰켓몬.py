def solution(nums):
    answer = 0
    ns=set(nums)
    if len(ns)>len(nums)//2:
        answer=len(nums)//2
    else:
        answer=len(ns)
    return answer