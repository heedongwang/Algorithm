def solution(num_list):
    answer = []
    last=num_list[-1]
    back2=num_list[-2]
    if last > back2:
        num_list.append((last-back2))
    else:
        num_list.append(2*last)
            
    return num_list