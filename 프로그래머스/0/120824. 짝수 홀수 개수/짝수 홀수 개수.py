def solution(num_list):
    answer = []
    even,odd=0,0
    for i in num_list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    answer=[even,odd]
    return answer