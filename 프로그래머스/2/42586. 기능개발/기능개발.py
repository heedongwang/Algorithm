def solution(progresses, speeds):
    answer = []
    day =[]
    for i, j in zip(progresses, speeds):
        if (100 - i) % j == 0:
            day.append((100 - i) // j)
        else:
            day.append((100 - i) // j + 1)

    print(day)
    
    count = 1
    while True:
        if len(day) > count and day[0] >= day[count]:
            count += 1
        elif len(day) > count and day[0] < day[count]:
            answer.append(count)
            day = day[count:]
            count = 1
        else:
            answer.append(count)
            break
    return answer