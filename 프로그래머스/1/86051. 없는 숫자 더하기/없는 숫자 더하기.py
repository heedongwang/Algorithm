def solution(numbers):
    
    alls=set([0,1,2,3,4,5,6,7,8,9])-set(numbers)
    return sum(alls)