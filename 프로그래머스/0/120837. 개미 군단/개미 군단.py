def solution(hp):
    gen=0
    cap=hp//5
    if hp%5>=3:
        gen=(hp%5)//3
        nor=(hp%5)%3
        print(nor)
    else:
        nor =hp%5
    answer=cap+gen+nor
    return answer