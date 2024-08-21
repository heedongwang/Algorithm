def solution(s):
    answer = True
    if 1<=len(s)<=8:
        if s.isdigit() and (len(s)==4 or len(s)==6):
            answer=True
        else:
            answer=False
    return answer